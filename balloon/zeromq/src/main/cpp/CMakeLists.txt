cmake_minimum_required(VERSION 2.8.4)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

find_path(ZMQ_INCLUDE_DIR
    NAMES
        zmq.h
    PATHS
        /usr/local/zeromq/include
)
message("ZeroMQ includes from ${ZMQ_INCLUDE_DIR}")

find_library(ZMQ_LIBRARY
    NAMES
        zmq
    PATHS
       /usr/local/zeromq/lib
)
message("ZeroMQ libs from ${ZMQ_LIBRARY}")

include_directories(${ZMQ_INCLUDE_DIR})
