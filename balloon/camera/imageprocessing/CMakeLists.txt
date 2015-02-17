cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing NONE)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --specs=nosys.specs")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --specs=nosys.specs")
set(CMAKE_SYSTEM_NAME Linux)

# TODO Set the path where OpenCV can be found.
IF(NOT DEFINED ENV{OpenCV_DIR})
    set(ENV{OpenCV_DIR} "/usr/local/opencv")
ENDIF(NOT DEFINED ENV{OpenCV_DIR})

MESSAGE("Using OpenCV from location: " $ENV{OpenCV_DIR})

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

set(SOURCE_FILES src/main.cpp)

add_executable(imageprocessing ${SOURCE_FILES})

target_link_libraries( imageprocessing ${OpenCV_LIBS} )