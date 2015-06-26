//
// Created by timoveldt on 6/26/15.
//


#include "zmq.hpp"

#include <iostream>
#include <sstream>
#include <unistd.h>

int main(int argc, char *argv[]) {
    zmq::context_t context(1);

    //  First, connect our subscriber socket
    zmq::socket_t publisher(context, ZMQ_PUB);
    publisher.connect("tcp://localhost:5560");

    const std::string topic = "CPP_TOPIC";
    for(int i = 5000; i< 6000; i++) {
        std::stringstream iss;

        publisher.send(topic.data(), topic.size(), ZMQ_SNDMORE);

        iss << i;
        const std::string message = iss.str();

        publisher.send(message.data(), message.size(), 0);

        iss.flush();

        usleep(250 * 100);
    }


    return 0;
}
