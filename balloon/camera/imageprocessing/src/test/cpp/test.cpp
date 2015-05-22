#include "gtest/gtest.h"

#include "imageprocessor.hpp"

using namespace imageprocessor;

TEST(test_images, test_images) {
    const Input *const input = new Input("/usr/local/jemoeder.jpg");
    const std::unique_ptr<const Result> result = imageprocessor::processImage(input);

    ASSERT_EQ(input->imageFile, result->imageFile);
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
