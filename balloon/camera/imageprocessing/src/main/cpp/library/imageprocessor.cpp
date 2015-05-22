#include "imageprocessor.hpp"

#include <opencv2/opencv.hpp>

namespace imageprocessor {
    std::unique_ptr<const Result> processImage(const Input *const input) {
        const Result *const result = new Result(false, input->imageFile, "Je UNIQUE moeder");

        std::unique_ptr<const Result> resultPtr(result);
        return std::move(resultPtr);
    }
}


