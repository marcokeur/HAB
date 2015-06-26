//
// Created by timoveldt on 6/17/15.
//

#include "zmq.hpp"

#include <iostream>
#include <sstream>
#include <unistd.h>

int main(int argc, char *argv[]) {
    zmq::context_t context(1);

    //  First, connect our subscriber socket
    zmq::socket_t subscriber(context, ZMQ_SUB);
    subscriber.setsockopt(ZMQ_SUBSCRIBE, "A", 1);
    subscriber.setsockopt(ZMQ_SUBSCRIBE, "D", 1);
    std::string topic = "CPP_TOPIC";
    subscriber.setsockopt(ZMQ_SUBSCRIBE, topic.data(), topic.size());
    subscriber.connect("tcp://localhost:5559");

    while (1) {
        zmq::message_t message(100);
        subscriber.recv(&message);

        std::string msg_str(static_cast<char*>(message.data()), message.size());


        std::cout << msg_str << std::endl;

        usleep(250 * 100);
    }


    return 0;
}