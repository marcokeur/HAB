#include "imageprocessor.hpp"
#include "../logging/logging.hpp"

#include <opencv2/opencv.hpp>

namespace imageprocessor {
    // Gets a quiet logger unless another cpp files specifies it first.
    const logging::Logger *const logger = logging::getLogger(IMAGE_PROCESSING_LOGGING_SOURCE);

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

    const int calculateMeanFrom1DimensionalHistogram(const Mat &histogram);

    const bool isHistogramClean(const Mat &image);

    const bool isImageSharpEnough(const Mat &image);

    const bool isGreyScaleHistogramClean(const Mat *image);

    ResultBuilder &analyzeImage(ResultBuilder &resultBuilder, const Mat &image);

    std::unique_ptr<const Result> processImage(const Input *const input) {
        logger->info("Processing " + input->imageFile);
        ResultBuilder resultBuilder;
        resultBuilder.sourceImageFile = input->imageFile;
        resultBuilder.send = false;
        resultBuilder.message = "Processing...";

        Mat image;
        image = imread(input->imageFile, CV_LOAD_IMAGE_ANYCOLOR);

        if (!image.data) {
            logger->warn("No image data, skipping actual processing... (image: " + input->imageFile + ").");
        } else {
            resultBuilder.message = "Starting analysis...";
            resultBuilder = analyzeImage(resultBuilder, image);
        }
        logger->info("Done with image, preparing to return result (image: " + input->imageFile + ").");
        std::unique_ptr<const Result> resultPtr(resultBuilder.build());
        return std::move(resultPtr);
    }

    ResultBuilder &analyzeImage(ResultBuilder &resultBuilder, const Mat &image) {
        Mat greyScale;
        cvtColor(image, greyScale, CV_RGB2GRAY);

        const bool sendForHistogram = isHistogramClean(image);
        const bool sendForGreyScaleHistogram = isGreyScaleHistogramClean(&greyScale);

//        const bool sendForSharpnessColor = isImageSharpEnough(image);
        const bool sendForSharpnessGreyScale = isImageSharpEnough(greyScale);

        resultBuilder.send =
                    sendForHistogram
                    && sendForGreyScaleHistogram
//                    && sendForSharpnessColor
                    && sendForSharpnessGreyScale;

        return resultBuilder;
    }

    /**
     *
     */
    const bool isImageSharpEnough(const Mat &image) {
        Mat sobelx, sobely;
        Sobel(image, sobelx, CV_32F, 1, 0, 3);
        Sobel(image, sobely, CV_32F, 0, 1, 3);
        magnitude(sobelx, sobely, sobelx);
        double sharpness = sum(sobelx)[0];

        std::stringstream ss;
        ss << "Sharpness for image: " << sharpness;
        logger->trace(ss.str());
        return sharpness > (1.5 * 1000000);
    }

    const int calculateMeanFrom1DimensionalHistogram(const Mat &histogram) {
        int sum = 0;
        int totalPixelCount = 0;
        for (int i = 0; i < histogram.rows; i++) {
            int pixelCount = cvRound(histogram.at<float>(i));
            sum += (i * pixelCount);
            totalPixelCount += pixelCount;
        }

        return sum / totalPixelCount;
    }

    const double calculateStandardDeviationFrom1DimensionalHistogram(const Mat &histogram, const int &mean) {
        int sum = 0;
        int totalPixelCount = 0;
        for (int i = 0; i < histogram.rows; i++) {
            int pixelCount = cvRound(histogram.at<float>(i));
            int diff = i - mean;
            sum += pixelCount * (diff * diff);
            totalPixelCount += pixelCount;
        }

        return sqrt(sum / totalPixelCount);
    }

    const bool isGreyScaleHistogramClean(const Mat *image) {
        int numberOfBins = 512;
        float range[] = {0, 512};
        const float *binRange = {range};

        bool uniform = true;
        bool accumulate = false;

        Mat histogram;
        calcHist(image, 1, 0, Mat(), histogram, 1, &numberOfBins, &binRange, uniform, accumulate);

        int mean = calculateMeanFrom1DimensionalHistogram(histogram);
        double std = calculateStandardDeviationFrom1DimensionalHistogram(histogram, mean);

        std::stringstream ss;
        ss << "Image mean: " << mean << " and std: " << std;
        logger->trace(ss.str());


        return (mean >= 100) && (std > 30);
    }

    const bool isHistogramClean(const Mat &image) {
        /// Separate the image in 3 places ( B, G and R )
        vector <Mat> bgr_planes;
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

        const int meanRed = calculateMeanFrom1DimensionalHistogram(r_hist);
        const int meanGreen = calculateMeanFrom1DimensionalHistogram(g_hist);
        const int meanBlue = calculateMeanFrom1DimensionalHistogram(b_hist);

        std::stringstream ss;
        ss << "Mean RGB values: " << meanRed << ", " << meanGreen << ", " << meanBlue;
        logger->trace(ss.str());

        // TODO: Analyze histogram.
        return true;
    }

    Result::~Result() {
        logger->trace("Destroying result");
    }
}

