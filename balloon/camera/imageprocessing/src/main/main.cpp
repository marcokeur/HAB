#include <unistd.h>
#include <sstream>
#include "../imageprocessing/imageprocessor.hpp"
#include "../logging/logging.hpp"
#include "zmq.hpp"

using namespace imageprocessor;
using namespace logging;

const Logger * const logger = getLogger("main", INFO);
const Logger * const image_processing_logger = getLogger(IMAGE_PROCESSING_LOGGING_SOURCE, INFO);

#ifndef INCOMING_TOPIC
#define INCOMING_TOPIC "/camera/picture/raw/location"
#endif /* INCOMING_TOPIC */

static const std::string IN_TOPIC = INCOMING_TOPIC;

#ifndef OUTGOING_TOPIC
#define OUTGOING_TOPIC "/camera/picture/processed/location"
#endif /* OUTGOING_TOPIC */

static const std::string OUT_TOPIC = OUTGOING_TOPIC;

int main(int argc, char **argv) {
    int pid = (int) getpid();
    std::stringstream ss;
    ss << "Started image processing module with pid " << pid;
    logger->info(ss.str());

    logger->info(IN_TOPIC);

    zmq::context_t context(1);

    zmq::socket_t subscriber(context, ZMQ_SUB);
    subscriber.setsockopt(ZMQ_SUBSCRIBE, IN_TOPIC.data(), IN_TOPIC.size());
    subscriber.connect("tcp://localhost:5559");

    zmq::socket_t publisher(context, ZMQ_PUB);
    publisher.connect("tcp://localhost:5560");

    zmq::message_t topic_header(4096);
    zmq::message_t message(4096);

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wmissing-noreturn"
    while(true) {
        subscriber.recv(&topic_header);
        std::string header_str(static_cast<char *>(topic_header.data()), topic_header.size());
        if(header_str.compare(IN_TOPIC) == 0) {
            subscriber.recv(&message);

            std::string msg_str(static_cast<char *>(message.data()), message.size());

            logger->info("Received location: " + msg_str);

            const Input *const input = new Input(msg_str);
            const std::unique_ptr<const Result> result = imageprocessor::processImage(input);

            logger->info(result->message);

            if (result->send) {
                logger->info("Sending for " + result->sourceImageFile + ": " + result->editedImageFile);
                publisher.send(OUT_TOPIC.data(), OUT_TOPIC.size(), ZMQ_SNDMORE);
                publisher.send(result->editedImageFile.data(), result->editedImageFile.size(), ZMQ_DONTWAIT);
            }
        }
    }
#pragma clang diagnostic pop

    logger->error("The image processing module is shutting down in a normal way...");
    context.close();
    logger->error("The image processing module went down in a normal way...");
    return 0;
}
