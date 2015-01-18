cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# TODO Set the path where OpenCV can be found.
set(ENV{OpenCV_DIR} "/usr/local/opencv")

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

set(SOURCE_FILES src/main.cpp)

add_executable(imageprocessing ${SOURCE_FILES})

target_link_libraries( imageprocessing ${OpenCV_LIBS} )