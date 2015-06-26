cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing_project)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

include_directories("logging")
include_directories("imageprocessing")

# Include zeromq.
include_directories(../../zeromq/include/)
include(../../zeromq/src/main/cpp/CMakeLists.txt)

add_subdirectory("src/main")
add_subdirectory("src/test")
add_subdirectory("src/logging")
add_subdirectory("src/imageprocessing")
