cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

IF(NOT DEFINED ENV{OpenCV_DIR})
    set(ENV{OpenCV_DIR} "/usr/local/opencv")
ENDIF(NOT DEFINED ENV{OpenCV_DIR})
MESSAGE("Using OpenCV from location: " $ENV{OpenCV_DIR} " (Override by exporting OpenCV_DIR)")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS} "src/main/cpp/imageprocessing")

file(GLOB MAIN_SOURCE_FILES "src/main/cpp/main.cpp")
file(GLOB IMAGE_PROCESSINGLIBRARY_SOURCE_FILES "src/main/cpp/imageprocessing/*.cpp")

add_executable(image_processing ${MAIN_SOURCE_FILES})
add_library(imageprocessing ${IMAGE_PROCESSINGLIBRARY_SOURCE_FILES})

target_link_libraries(imageprocessing ${OpenCV_LIBS})
target_link_libraries(image_processing imageprocessing)

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

##############
# Unit Tests
##############
file(GLOB TEST_SOURCE_FILES "src/test/cpp/*.cpp")
file(GLOB GENERATED_TEST_SOURCE_FILES "src/test/gen/cpp/*.cpp")
add_executable(runUnitTests ${TEST_SOURCE_FILES} ${GENERATED_TEST_SOURCE_FILES})
target_link_libraries(runUnitTests gtest gtest_main imageprocessing)

add_test(NAME test_images COMMAND runUnitTests)
add_test(NAME test_file COMMAND runUnitTests)

