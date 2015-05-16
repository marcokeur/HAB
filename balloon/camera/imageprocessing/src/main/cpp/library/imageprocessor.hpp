#ifndef IMAGEPROCESSOR_H
#define IMAGEPROCESSOR_H

#include <string>
#include <memory>

#ifdef TRACE_LOGGING // TODO fix logging and debug builds.
#include <iostream>
#endif /* TRACE_LOGGING */

namespace imageprocessor {
	class Result {
		public:
			const bool send;
			const std::string imageFile;
			const std::string message;
			Result(bool send, std::string imageFile, std::string message) : send{send}, imageFile{imageFile}, message{message} {}
#ifdef TRACE_LOGGING
			~Result() {
				std::cout << "Destroying Result" <<std::endl;
			}
#endif /* TRACE_LOGGING */
	};

	class Input {
		public:
			const std::string imageFile;
			Input(std::string imageFile) : imageFile{imageFile} {}
	};

	//const Result* const processImage(const Input* const input);
        std::unique_ptr<const Result> processImage(const Input* const input);
}

#endif /* IMAGEPROCESSOR_H */
