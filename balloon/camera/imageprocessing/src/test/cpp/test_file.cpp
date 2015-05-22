//
// Created by timoveldt on 5/22/15.
//

#include "gtest/gtest.h"

#include "imageprocessor.hpp"

using namespace imageprocessor;

TEST(test_file, test_correct_file_name) {
    const Input *const input = new Input("/usr/local/jemoeder.jpg");
    const std::unique_ptr<const Result> result = imageprocessor::processImage(input);

    ASSERT_EQ(input->imageFile, result->sourceImageFile);
}

TEST(test_file, test_correct_file_name_again) {
    const Input *const input = new Input("/usr/local/jemoeder2.jpg");
    const std::unique_ptr<const Result> result = imageprocessor::processImage(input);

    ASSERT_EQ(input->imageFile, result->sourceImageFile);
}