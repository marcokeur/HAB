#include "imageprocessor.hpp"

#include <opencv2/opencv.hpp>

namespace imageprocessor {
    using namespace cv;

    std::unique_ptr<const Result> processImage(const Input *const input) {
        const Result *const result = new Result(false, input->imageFile, "Je UNIQUE moeder");

        Mat image;
        image = imread(input->imageFile, 1);

        /// Separate the image in 3 places ( B, G and R )
//        vector<Mat> bgr_planes;
//        split(image, bgr_planes);
//
//        /// Establish the number of bins
//        int histSize = 256;
//
//        /// Set the ranges ( for B,G,R) )
//        float range[] = {0, 256};
//        const float *histRange = {range};
//
//        bool uniform = true;
//        bool accumulate = false;
//
//        Mat b_hist, g_hist, r_hist;
//
//        /// Compute the histograms:
//        calcHist(&bgr_planes[0], 1, 0, Mat(), b_hist, 1, &histSize, &histRange, uniform, accumulate);
//        calcHist(&bgr_planes[1], 1, 0, Mat(), g_hist, 1, &histSize, &histRange, uniform, accumulate);
//        calcHist(&bgr_planes[2], 1, 0, Mat(), r_hist, 1, &histSize, &histRange, uniform, accumulate);


        std::unique_ptr<const Result> resultPtr(result);
        return std::move(resultPtr);
    }
}


