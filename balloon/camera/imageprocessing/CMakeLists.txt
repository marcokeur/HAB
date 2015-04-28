cmake_minimum_required(VERSION 2.8.4)
project(imageprocessing)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# TODO Set the path where OpenCV can be found.
IF(NOT DEFINED ENV{OpenCV_DIR})
    set(ENV{OpenCV_DIR} "/usr/local/opencv")
ENDIF(NOT DEFINED ENV{OpenCV_DIR})
MESSAGE("Using OpenCV from location: " $ENV{OpenCV_DIR})

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

set(SOURCE_FILES src/main/cpp/main.cpp)
add_executable(imageprocessing ${SOURCE_FILES})
target_link_libraries( imageprocessing ${OpenCV_LIBS} )

##########
# TESTING
##########
enable_testing()
set(PROJECT_TEST_NAME ${PROJECT_NAME_STR}_test)
file(GLOB TEST_SOURCE_FILES ${PROJECT_SOURCE_DIR}/test/*.cpp)

add_executable(${PROJECT_TEST_NAME} ${TEST_SOURCE_FILES})
add_dependencies(${PROJECT_TEST_NAME} googletest)

# TODO Set the path where GTEST_INCLUDE can be found.
IF(NOT DEFINED ENV{GTEST_INCLUDE_DIR})
    set(ENV{GTEST_INCLUDE_DIR} "/usr/local/include/gtest")
ENDIF(NOT DEFINED ENV{GTEST_INCLUDE_DIR})
MESSAGE("Using Google Test includes from location: " $ENV{GTEST_INCLUDE_DIR})

# TODO Set the path where GTEST_LIB can be found.
IF(NOT DEFINED ENV{GTEST_LIBS_DIR})
    set(ENV{GTEST_LIBS_DIR} "/usr/local/lib/gtest")
ENDIF(NOT DEFINED ENV{GTEST_LIBS_DIR})
MESSAGE("Using Google Test libs from location: " $ENV{GTEST_LIBS_DIR})

# Include google test.
include_directories( ${GTEST_INCLUDE_DIR} )
target_link_libraries(${PROJECT_TEST_NAME} ${GTEST_LIBS_DIR}/gtest ${GTEST_LIBS_DIR}/gtest_main)

add_test(test_images ${PROJECT_TEST_NAME})

