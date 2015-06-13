#include "gtest/gtest.h"

#include "../imageprocessing/imageprocessor.hpp"
#include "../logging/logging.hpp"

using namespace imageprocessor;
using namespace logging;

const Logger * const image_processing_logger = getLogger(IMAGE_PROCESSING_LOGGING_SOURCE, TRACE);

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
