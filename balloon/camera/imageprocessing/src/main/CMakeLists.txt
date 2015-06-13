cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

add_definitions(-DLOGGER_LEVEL=INFO)

IF(NOT DEFINED ENV{OpenCV_DIR})
    set(ENV{OpenCV_DIR} "/usr/local/opencv")
ENDIF(NOT DEFINED ENV{OpenCV_DIR})
MESSAGE("Using OpenCV from location: " $ENV{OpenCV_DIR} " (Override by exporting OpenCV_DIR)")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

file(GLOB LOGGING_SOURCE_FILES "cpp/logging/*.cpp")
add_library(logging ${LOGGING_SOURCE_FILES})
include_directories("cpp/logging")

file(GLOB IMAGE_PROCESSINGLIBRARY_SOURCE_FILES "cpp/imageprocessing/*.cpp")
add_library(imageprocessing ${IMAGE_PROCESSINGLIBRARY_SOURCE_FILES})
target_link_libraries(imageprocessing ${OpenCV_LIBS} logging)
include_directories("cpp/imageprocessing")

file(GLOB MAIN_SOURCE_FILES "cpp/main.cpp")
add_executable(image_processing ${MAIN_SOURCE_FILES})
target_link_libraries(image_processing imageprocessing logging)
