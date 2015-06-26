cmake_minimum_required(VERSION 2.8.4)
project(zeromq_example)

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

file(GLOB SUBSCRIBER_SOURCE_FILES "subscriber.cpp")
add_executable(zeromq_subscriber ${SUBSCRIBER_SOURCE_FILES})
target_link_libraries(zeromq_subscriber ${ZMQ_LIBRARY})

file(GLOB PUBLISHER_SOURCE_FILES "publisher.cpp")
add_executable(zeromq_publisher ${PUBLISHER_SOURCE_FILES} publisher.h publisher.cpp)
target_link_libraries(zeromq_publisher ${ZMQ_LIBRARY})
