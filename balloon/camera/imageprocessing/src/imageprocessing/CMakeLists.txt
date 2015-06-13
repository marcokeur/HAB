cmake_minimum_required(VERSION 2.8.4)
project(logging)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

IF(NOT DEFINED ENV{OpenCV_DIR})
    set(ENV{OpenCV_DIR} "/usr/local/opencv")
ENDIF(NOT DEFINED ENV{OpenCV_DIR})
MESSAGE("Using OpenCV from location: " $ENV{OpenCV_DIR} " (Override by exporting OpenCV_DIR)")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

file(GLOB IMAGE_PROCESSINGLIBRARY_SOURCE_FILES "../imageprocessing/*.cpp")
add_library(imageprocessing ${IMAGE_PROCESSINGLIBRARY_SOURCE_FILES})
target_link_libraries(imageprocessing ${OpenCV_LIBS} logging)
