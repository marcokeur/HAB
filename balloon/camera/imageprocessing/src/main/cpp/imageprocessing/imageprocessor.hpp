#ifndef IMAGEPROCESSOR_H
#define IMAGEPROCESSOR_H

#include <string>
#include <memory>

#ifdef TRACE_LOGGING // TODO fix logging and debug builds.
#include <logging.hpp>

static const logging::Logger * const logger = logging::getLogger("imageprocessing");
#endif /* TRACE_LOGGING */

namespace imageprocessor {
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

#ifdef TRACE_LOGGING
			~Result() {
				logger->trace("Destroying result");
			}
#endif /* TRACE_LOGGING */
    };

    class Input {
    public:
        const std::string imageFile;

        Input(std::string imageFile) : imageFile{imageFile} { }
    };

    //const Result* const processImage(const Input* const input);
    std::unique_ptr<const Result> processImage(const Input *const input);
}

#endif /* IMAGEPROCESSOR_H */
