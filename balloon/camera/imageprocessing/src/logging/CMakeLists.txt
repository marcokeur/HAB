cmake_minimum_required(VERSION 2.8.4)
project(logging)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

file(GLOB LOGGING_SOURCE_FILES "*.cpp")
add_library(logging ${LOGGING_SOURCE_FILES})
