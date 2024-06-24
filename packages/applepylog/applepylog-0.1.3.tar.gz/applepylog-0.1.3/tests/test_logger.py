import sys

import pytest
from applepylog.logger import Logger, LogLevel
from io import StringIO
from typing import TextIO


class TestLogger:
    writer: TextIO

    @pytest.fixture(autouse=True)
    def setup_writer(self):
        self.writer = StringIO()
        yield
        self.writer = StringIO()

    def test_info_logger_with_same_level(self):
        _logger = Logger("Test Logger", LogLevel.INFO, self.writer)
        _logger.info("test message")
        self.writer.seek(0)
        assert "INFO Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_warn_logger_with_same_level(self):
        _logger = Logger("Test Logger", LogLevel.WARN, self.writer)
        _logger.warn("test message")
        self.writer.seek(0)
        assert "WARN Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_debug_logger_with_same_level(self):
        _logger = Logger("Test Logger", LogLevel.DEBUG, self.writer)
        _logger.debug("test message")
        self.writer.seek(0)
        assert "DEBUG Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_error_logger_with_same_level(self):
        _logger = Logger("Test Logger", LogLevel.ERROR, self.writer)
        _logger.error("test message")
        self.writer.seek(0)
        assert "ERROR Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_default_level_info_logger(self):
        _logger = Logger("Test Logger", writer=self.writer)
        _logger.info("test message")
        self.writer.seek(0)
        assert "INFO Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_default_level_warn_logger(self):
        _logger = Logger("Test Logger", writer=self.writer)
        _logger.warn("test message")
        self.writer.seek(0)
        assert "WARN Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_default_level_debug_logger(self):
        _logger = Logger("Test Logger", writer=self.writer)
        _logger.debug("test message")
        self.writer.seek(0)
        assert "" == self.writer.read()

    def test_default_level_error_logger(self):
        _logger = Logger("Test Logger", writer=self.writer)
        _logger.error("test message")
        self.writer.seek(0)
        assert "ERROR Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_error_level_info_logger(self):
        _logger = Logger("Test Logger", LogLevel.ERROR, writer=self.writer)
        _logger.info("test message")
        self.writer.seek(0)
        assert "" == self.writer.read()

    def test_error_level_warn_logger(self):
        _logger = Logger("Test Logger", LogLevel.ERROR, writer=self.writer)
        _logger.warn("test message")
        self.writer.seek(0)
        assert "" == self.writer.read()

    def test_error_level_debug_logger(self):
        _logger = Logger("Test Logger", LogLevel.ERROR, writer=self.writer)
        _logger.debug("test message")
        self.writer.seek(0)
        assert "" == self.writer.read()

    def test_error_level_error_logger(self):
        _logger = Logger("Test Logger", LogLevel.ERROR, writer=self.writer)
        _logger.error("test message")
        self.writer.seek(0)
        assert "ERROR Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_debug_level_info_logger(self):
        _logger = Logger("Test Logger", LogLevel.DEBUG, writer=self.writer)
        _logger.info("test message")
        self.writer.seek(0)
        assert "INFO Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_debug_level_warn_logger(self):
        _logger = Logger("Test Logger", LogLevel.DEBUG, writer=self.writer)
        _logger.warn("test message")
        self.writer.seek(0)
        assert "WARN Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_debug_level_error_logger(self):
        _logger = Logger("Test Logger", LogLevel.DEBUG, writer=self.writer)
        _logger.error("test message")
        self.writer.seek(0)
        assert "ERROR Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_debug_level_debug_logger(self):
        _logger = Logger("Test Logger", LogLevel.DEBUG, writer=self.writer)
        _logger.debug("test message")
        self.writer.seek(0)
        assert "DEBUG Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_stdout_info_level_info_logger(self, capsys):
        _logger = Logger("Test Logger", LogLevel.INFO, sys.stdout)
        _logger.info("test message")
        logged = capsys.readouterr()
        assert "INFO Test Logger, test message\n" == logged.out[27:]  # ignoring timestamp

    def test_alt_writer_info_level_info_logger(self, capsys):
        _logger = Logger("Test Logger", LogLevel.INFO, sys.stdout, LogLevel.INFO, self.writer)
        _logger.info("test message")
        self.writer.seek(0)
        logged = capsys.readouterr()
        assert "INFO Test Logger, test message\n" == logged.out[27:]  # ignoring timestamp
        assert "INFO Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp

    def test_write_file_info_level_info_logger(self):
        file = open("./test.txt", "w+")
        _logger = Logger("Test Logger", LogLevel.INFO, file)
        _logger.info("test message")
        file.seek(0)
        assert "INFO Test Logger, test message\n" == file.read()[27:]  # ignoring timestamp
        file.close()

    def test_multi_write_file_info_level_logger(self):
        file = open("./test.txt", "w+")
        _logger = Logger("Test Logger", LogLevel.INFO, file)
        _logger.info("test message")
        _logger.info("other test message")
        file.seek(0)
        assert ("INFO Test Logger, test message INFO Test Logger, other test message " ==
                ' '.join([line[27:] for line in file.read().split('\n')]))  # ignoring timestamps
        file.close()

    def test_different_log_level_writers(self, capsys):
        _logger = Logger("Test Logger", LogLevel.ERROR, sys.stdout, LogLevel.INFO, self.writer)
        _logger.info("test message")
        self.writer.seek(0)
        logged = capsys.readouterr()
        assert "" == logged.out  # ignoring timestamp
        assert "INFO Test Logger, test message\n" == self.writer.read()[27:]  # ignoring timestamp