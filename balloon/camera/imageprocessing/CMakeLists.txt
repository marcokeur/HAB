cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

IF(NOT DEFINED ENV{OpenCV_DIR})
    set(ENV{OpenCV_DIR} "/usr/local/opencv")
ENDIF(NOT DEFINED ENV{OpenCV_DIR})
MESSAGE("Using OpenCV from location: " $ENV{OpenCV_DIR} " (Override by exporting OpenCV_DIR)")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

file(GLOB MAIN_SOURCE_FILES "src/main/cpp/main.cpp")
file(GLOB LIBRARY_SOURCE_FILES "src/main/cpp/library/*.cpp")

add_executable(imageprocessing ${MAIN_SOURCE_FILES})
add_library(imageprocessing_library ${LIBRARY_SOURCE_FILES})

target_link_libraries(imageprocessing ${OpenCV_LIBS} imageprocessing_library)

##########
# TESTING
##########
enable_testing()

IF(NOT DEFINED ENV{GOOGLETEST_DIR})
    set(ENV{GOOGLETEST_DIR} "/usr/local/googletest/gtest-1.7.0")
ENDIF(NOT DEFINED ENV{GOOGLETEST_DIR})
MESSAGE("Using Google Test from location: " $ENV{GOOGLETEST_DIR} " (Override by exporting GOOGLETEST_DIR)")

# Add googletest through subdirectory.
add_subdirectory("$ENV{GOOGLETEST_DIR}" "${CMAKE_CURRENT_BINARY_DIR}/googletest")
# Includes through imported project
include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})

# Add googletest through external project
#include(ExternalProject)
#ExternalProject_Add(googletest
#    SOURCE_DIR $ENV{GOOGLETEST_DIR}
#    BINARY_DIR "${CMAKE_CURRENT_BINARY_DIR}/googletest"
#    INSTALL_COMMAND ""
#)
#include_directories($ENV{GOOGLETEST_DIR}/include $ENV{GOOGLETEST_DIR})

##############
# Unit Tests
##############
file(GLOB TEST_SOURCE_FILES "src/test/cpp/*.cpp")
add_executable(runUnitTests ${TEST_SOURCE_FILES})
target_link_libraries(runUnitTests gtest gtest_main imageprocessing_library)

add_test(NAME test_images COMMAND runUnitTests)

add_subdirectory(src/main/cpp/library/include)