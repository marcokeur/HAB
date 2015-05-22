#include "imageprocessor.hpp"

#include <opencv2/opencv.hpp>

namespace imageprocessor {

    using namespace cv;

    class ResultBuilder {
    public:
        bool send;
        std::string sourceImageFile;
        std::string editedImageFile;
        std::string message;

        const Result *const build() {
            return new Result(send, sourceImageFile, editedImageFile, message);
        }
    };

    int calculateColorMeanFrom1DimensionalHistogram(int numberOfBins, Mat &histogram);

    std::unique_ptr<const Result> processImage(const Input *const input) {
        ResultBuilder resultBuilder;
        resultBuilder.sourceImageFile = input->imageFile;
        resultBuilder.send = false;
        resultBuilder.message = "Processing...";

        Mat image;
        image = imread(input->imageFile, CV_LOAD_IMAGE_ANYCOLOR);

        if (!image.data) {
            resultBuilder.message = "No image data, aborted...";
        } else {

            /// Separate the image in 3 places ( B, G and R )
            vector<Mat> bgr_planes;
            split(image, bgr_planes);

            /// Establish the number of bins
            int histSize = 256;

            /// Set the ranges ( for B,G,R) )
            float range[] = {0, 256};
            const float *histRange = {range};

            bool uniform = true;
            bool accumulate = false;

            Mat b_hist, g_hist, r_hist;

            /// Compute the histograms:
            calcHist(&bgr_planes[0], 1, 0, Mat(), b_hist, 1, &histSize, &histRange, uniform, accumulate);
            calcHist(&bgr_planes[1], 1, 0, Mat(), g_hist, 1, &histSize, &histRange, uniform, accumulate);
            calcHist(&bgr_planes[2], 1, 0, Mat(), r_hist, 1, &histSize, &histRange, uniform, accumulate);

            int hist_h = 400;
            /// Normalize the result to [ 0, histImage.rows ]
            normalize(b_hist, b_hist, 0, hist_h, NORM_MINMAX, -1, Mat());
            normalize(g_hist, g_hist, 0, hist_h, NORM_MINMAX, -1, Mat());
            normalize(r_hist, r_hist, 0, hist_h, NORM_MINMAX, -1, Mat());

            int meanRed = calculateColorMeanFrom1DimensionalHistogram(histSize, r_hist);
            int meanGreen = calculateColorMeanFrom1DimensionalHistogram(histSize, g_hist);
            int meanBlue = calculateColorMeanFrom1DimensionalHistogram(histSize, b_hist);
        }
        std::unique_ptr<const Result> resultPtr(resultBuilder.build());
        return std::move(resultPtr);
    }

    int calculateColorMeanFrom1DimensionalHistogram(int numberOfBins, Mat &histogram) {
        int sum = 0;
        int totalPixelCount = 0;
        for (int i = 0; i < numberOfBins; i++) {
                int pixelCount = cvRound(histogram.at<float>(i));
                std::cout << i << ": " << pixelCount << std::endl;
                sum += (i * pixelCount);
                totalPixelCount += pixelCount;
            }

        return sum / totalPixelCount;
    }
}


