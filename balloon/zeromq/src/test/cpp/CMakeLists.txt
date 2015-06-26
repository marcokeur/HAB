cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing)

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
file(GLOB MAIN_SOURCE_FILES "main.cpp")
add_executable(zeromq_tester ${MAIN_SOURCE_FILES})
target_link_libraries(zeromq_tester ${ZMQ_LIBRARY})
