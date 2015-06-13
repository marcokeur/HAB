//
// Created by timoveldt on 5/29/15.
//

#ifndef IMAGEPROCESSING_LOGGING_HPP
#define IMAGEPROCESSING_LOGGING_HPP

#include <string>

namespace logging {
    enum LoggingLevel {
        QUIET, ERROR, WARN, INFO, DEBUG, TRACE
    };

    class Logger {
    public:
        virtual void trace(const std::string &format) const = 0;

        virtual void debug(const std::string &format) const = 0;

        virtual void info(const std::string &format) const = 0;

        virtual void warn(const std::string &format) const = 0;

        virtual void error(const std::string &format) const = 0;
    };

    const Logger *const getLogger(const std::string &source, const LoggingLevel &level=QUIET);
}

#endif //IMAGEPROCESSING_LOGGING_HPP
