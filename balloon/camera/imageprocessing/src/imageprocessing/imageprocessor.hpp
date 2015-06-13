#ifndef IMAGEPROCESSOR_H
#define IMAGEPROCESSOR_H

#include <string>
#include <memory>

namespace imageprocessor {
    const std::string IMAGE_PROCESSING_LOGGING_SOURCE = "imageprocessing";

    class Result {
    public:
        const bool send;
        const std::string sourceImageFile;
        const std::string editedImageFile;
        const std::string message;

        Result(bool send, std::string sourceImageFile, std::string editedImageFile, std::string message)
                : send{send},
                  sourceImageFile{
                          sourceImageFile},
                  editedImageFile{
                          editedImageFile},
                  message{message} { }

        ~Result();
    };

    class Input {
    public:
        const std::string imageFile;

        Input(std::string imageFile) : imageFile{imageFile} { }
    };

    std::unique_ptr<const Result> processImage(const Input *const input);
}

#endif /* IMAGEPROCESSOR_H */
