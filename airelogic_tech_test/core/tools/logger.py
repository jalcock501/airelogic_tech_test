""" Logging singleton for CLI """
import logging
import os
import datetime
import time


class Logger:
    """ Custom Logging Class """
    _logger = None

    def __new__(cls, logging_level="INFO",
                _file="airelogicTT.log",
                *args, **kwargs):
        if cls._logger is None:

            cls._logger = super().__new__(cls, *args, **kwargs)
            cls._logger = logging.getLogger("TechTest")
            cls._logger.setLevel(logging_level)
            formatter = logging.Formatter(
                '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

            now = datetime.datetime.now()

            fileHandler = logging.FileHandler(_file)
            fileHandler.setFormatter(formatter)
            cls._logger.addHandler(fileHandler)

            # sets up an IO stream but messes with the progress bars
            if kwargs.get('stream'):
                streamHandler = logging.StreamHandler()
                streamHandler.setFormatter(formatter)
                cls._logger.addHandler(streamHandler)

        return cls._logger
