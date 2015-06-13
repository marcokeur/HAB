cmake_minimum_required(VERSION 2.8.4)
project(unit_tests)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

enable_testing()

# Google test
IF(NOT DEFINED ENV{GOOGLETEST_DIR})
    set(ENV{GOOGLETEST_DIR} "/usr/local/googletest/gtest-1.7.0")
ENDIF(NOT DEFINED ENV{GOOGLETEST_DIR})
MESSAGE("Using Google Test from location: " $ENV{GOOGLETEST_DIR} " (Override by exporting GOOGLETEST_DIR)")

# Add googletest through subdirectory.
add_subdirectory("$ENV{GOOGLETEST_DIR}" "${CMAKE_CURRENT_BINARY_DIR}/test/googletest")
# Includes through imported project
include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})

##############
# Unit Tests
##############
file(GLOB TEST_SOURCE_FILES "*.cpp")
file(GLOB GENERATED_TEST_SOURCE_FILES "gen/cpp/*.cpp")

add_executable(runUnitTests ${TEST_SOURCE_FILES} ${GENERATED_TEST_SOURCE_FILES})
target_link_libraries(runUnitTests gtest gtest_main imageprocessing)

add_test(NAME test_images COMMAND runUnitTests)
add_test(NAME test_file COMMAND runUnitTests)


