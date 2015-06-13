#include "../imageprocessing/imageprocessor.hpp"
#include "../logging/logging.hpp"

using namespace imageprocessor;
using namespace logging;

const Logger * const logger = getLogger("main", INFO);
const Logger * const image_processing_logger = getLogger(IMAGE_PROCESSING_LOGGING_SOURCE, INFO);

int main(int argc, char **argv) {
    logger->info("Started main...");
    const Input *const input = new Input("/usr/local/jemoeder.jpg");
    const std::unique_ptr<const Result> result = imageprocessor::processImage(input);

    logger->info(result->message);

    return 0;
}
