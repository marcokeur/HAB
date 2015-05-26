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

    const int calculateColorMeanFrom1DimensionalHistogram(const int numberOfBins, const Mat &histogram);
    const bool isHistogramClean(const Mat &image);
    const bool isImageSharpEnough(const Mat &image);

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
            Mat greyScale;
            cvtColor(image, greyScale, CV_RGB2GRAY);
            
            const bool sendForHistogram = isHistogramClean(image);
            
            //const bool sendForSharpnessColor = isImageSharpEnough(image);
            const bool sendForSharpnessGreyScale = isImageSharpEnough(greyScale);
            
            resultBuilder.send = 
            sendForHistogram 
            //&& sendForSharpnessColor 
            && sendForSharpnessGreyScale
            ;
        }
        std::unique_ptr<const Result> resultPtr(resultBuilder.build());
        return std::move(resultPtr);
    }

    /**
     *
     */
    const bool isImageSharpEnough(const Mat &image) {
        Mat sobelx, sobely;
        Sobel(image, sobelx, image.depth(), 1, 0);
        Sobel(image, sobely, image.depth(), 0, 1);
        magnitude(sobelx,sobely,sobelx);
        double sharpness = sum(sobelx)[0];    
    
//        Mat dx,dy;
  //      Sobel(image,dx,1,0,3,image.depth());
    //    Sobel(image,dy,0,1,3,image.depth());
      //  magnitude(dx,dy,dx);
      //  double sharpness = sum(dx)[0];
        std::cout << "Sharpness for image: " << sharpness << std::endl;
        return sharpness > (2.0*1000000);
    }

    const int calculateColorMeanFrom1DimensionalHistogram(const int numberOfBins, const Mat &histogram) {
        int sum = 0;
        int totalPixelCount = 0;
        for (int i = 0; i < numberOfBins; i++) {
                int pixelCount = cvRound(histogram.at<float>(i));
                // std::cout << i << ": " << pixelCount << std::endl;
                sum += (i * pixelCount);
                totalPixelCount += pixelCount;
            }

        return sum / totalPixelCount;
    }

    const bool isHistogramClean(const Mat &image) {
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

        const int meanRed = calculateColorMeanFrom1DimensionalHistogram(histSize, r_hist);
        const int meanGreen = calculateColorMeanFrom1DimensionalHistogram(histSize, g_hist);
        const int meanBlue = calculateColorMeanFrom1DimensionalHistogram(histSize, b_hist);
        
        
        
        // TODO: Analyze histogram.
        return true;
    }
}

