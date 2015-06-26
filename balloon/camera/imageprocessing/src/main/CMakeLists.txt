cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

file(GLOB MAIN_SOURCE_FILES "main.cpp")
add_executable(image_processing ${MAIN_SOURCE_FILES})
target_link_libraries(image_processing imageprocessing logging ${ZMQ_LIBRARY})
