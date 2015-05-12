#include "imageprocessor.hpp"

#include <opencv2/opencv.hpp>

namespace imageprocessor {
	const Result* const processImage(const Input* const input) {
		const Result* const result = new Result(false, input->imageFile, "JE MOEDER");

		return result;
	}
}


