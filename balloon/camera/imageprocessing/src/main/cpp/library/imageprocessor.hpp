#ifndef IMAGEPROCESSOR_H
#define IMAGEPROCESSOR_H

#include <string>

namespace imageprocessor {
	class Result {
		public:
			const bool send;
			const std::string imageFile;
			const std::string message;
			Result(bool send, std::string imageFile, std::string message) : send{send}, imageFile{imageFile}, message{message} {}
	};

	class Input {
		public:
			const std::string imageFile;
			Input(std::string imageFile) : imageFile{imageFile} {}
	};

	const Result* const processImage(const Input* const input);
}

#endif /* IMAGEPROCESSOR_H */
