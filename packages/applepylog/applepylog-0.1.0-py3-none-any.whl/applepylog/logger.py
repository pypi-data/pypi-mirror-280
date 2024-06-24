import sys
from datetime import datetime
from enum import Enum
from typing import TextIO


class LogLevel(Enum):
    ERROR = 0
    INFO = 1
    WARN = 2
    DEBUG = 3


class Logger:
    writer: TextIO
    alt_writer: TextIO
    logger_name: str
    log_level: LogLevel
    alt_log_level: LogLevel

    def __init__(self, logger_name: str, log_level: LogLevel = LogLevel.WARN, writer: TextIO = sys.stdout,
                 alt_log_level: LogLevel = LogLevel.WARN, alt_writer: TextIO = None):
        self.logger_name = logger_name
        self.writer = writer
        self.alt_writer = alt_writer
        self.log_level = log_level
        self.alt_log_level = alt_log_level

    def __build_basic_message(self, message: str, log_level: LogLevel) -> str:
        return f"{datetime.now()} {log_level.name} {self.logger_name}, {message}\n"

    def __log_message(self, message: str, log_lvl: LogLevel):
        out_msg = ""
        if self.log_level.value >= log_lvl.value:
            out_msg = self.__build_basic_message(message, log_lvl)
            self.writer.write(out_msg)
        if self.alt_writer is not None and self.alt_log_level.value >= log_lvl.value:
            self.alt_writer.write(out_msg if out_msg else self.__build_basic_message(message, log_lvl))

    def info(self, message: str):
        self.__log_message(message, LogLevel.INFO)

    def warn(self, message: str):
        self.__log_message(message, LogLevel.WARN)

    def debug(self, message: str):
        self.__log_message(message, LogLevel.DEBUG)

    def error(self, message: str):
        self.__log_message(message, LogLevel.ERROR)
