//
// Created by timoveldt on 5/29/15.
//

#include "logging.hpp"

#include <vector>
#include <map>
#include <memory>
#include <iostream>
#include <sstream>
#include <iomanip>

#include <mutex>

namespace logging {
    std::mutex loggingMutex;

    class LoggerImpl : Logger {
    public:
        const std::string source;

        LoggerImpl(std::string source) : source(source) { }

        ~LoggerImpl() {
            this->trace("Closed logger.");
        }

    private:
        virtual void trace(const std::string &format) const override;

        virtual void debug(const std::string &format) const override;

        virtual void info(const std::string &format) const override;

        virtual void warn(const std::string &format) const override;

        virtual void error(const std::string &format) const override;

        void log(const std::string &level, const std::string &format) const;
    };


    struct LoggerComparator {
        bool operator()(const std::unique_ptr<const LoggerImpl> &lhs,
                        const std::unique_ptr<const LoggerImpl> &rhs) const {
            return lhs->source.compare(rhs->source) == 0;
        }
    };

    const Logger *const getLogger(const std::string &source) {
        static std::vector<std::unique_ptr<const LoggerImpl>> loggers;
        static std::map<std::string, const LoggerImpl*> loggerMap;

        const LoggerImpl *instance = loggerMap[source];
        if(instance == 0) {
            instance = new LoggerImpl(source);
            loggerMap[source] = instance;
            std::unique_ptr<const LoggerImpl> logger(instance);
            loggers.push_back(std::move(logger));
        }

        return (const Logger *const) instance;
    }

    void streamTime(std::stringstream &stream) {
        time_t t = time(0);   // get time now
        struct tm *now = localtime(&t);

        stream
        << (now->tm_year + 1900) << '-'
        << std::setw(2) << std::setfill('0') << (now->tm_mon + 1) << '-'
        << std::setw(2) << std::setfill('0') << now->tm_mday << " "
        << std::setw(2) << std::setfill('0') << now->tm_hour << ":"
        << std::setw(2) << std::setfill('0') << now->tm_mday << ":"
        << std::setw(2) << std::setfill('0') << now->tm_sec << " - ";
    }

    void LoggerImpl::trace(const std::string &format) const {
        log("TRACE", format);
    }

    void LoggerImpl::debug(const std::string &format) const {
        log("DEBUG", format);
    }

    void LoggerImpl::info(const std::string &format) const {
        log("INFO", format);
    }

    void LoggerImpl::warn(const std::string &format) const {
        log("WARN", format);
    }

    void LoggerImpl::error(const std::string &format) const {
        log("ERROR", format);
    }

    void LoggerImpl::log(const std::string &level, const std::string &format) const {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunused-variable"
        std::lock_guard<std::mutex> lockGuard(loggingMutex);
#pragma clang diagnostic pop
        std::stringstream stream;
        streamTime(stream);
        stream << source << " " << level << " - " << format << std::endl;

        std::cout << stream.str();
    }
}