# a logger class that prints to stdout and to a file
# it provides a simple interface to log messages
# info, debug, warning, error, critical

import logging
import sys
import os
import datetime
import traceback
import json

class Logger:
    def __init__(self, name, log_file=None):
        self.name = name
        self.log_file = log_file
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.stream_handler = logging.StreamHandler(sys.stdout)
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)
        if log_file is not None:
            self.file_handler = logging.FileHandler(log_file)
            self.file_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.file_handler)

    def info(self, msg):
        self.logger.info(msg)
        self.write_to_file(msg, "INFO")

    def debug(self, msg):
        self.logger.debug(msg)
        self.write_to_file(msg, "DEBUG")

    def warning(self, msg):
        self.logger.warning(msg)
        self.write_to_file(msg, "WARNING")

    def error(self, msg):
        self.logger.error(msg)
        self.write_to_file(msg, "ERROR")

    def critical(self, msg):
        self.logger.critical(msg)
        self.write_to_file(msg, "CRITICAL")

    def exception(self, msg):
        self.logger.exception(msg)
        self.write_to_file(msg, "EXCEPTION")

    def write_to_file(self, msg, level):
        if self.log_file is not None:
            with open(self.log_file, "a") as f:
                f.write(f"{datetime.datetime.now()} - {level} - {msg}\n")

    def log_exception(self, e):
        self.exception(f"Exception: {e}")
        self.exception(f"Traceback: {traceback.format_exc()}")

    def log_request(self, request):
        self.info(f"Request: {request}")
        self.info(f"Request headers: {request.headers}")
        self.info(f"Request body: {request.get_data()}")

    def log_response(self, response):
        self.info(f"Response: {response}")

    def log_json(self, json):
        self.info(f"JSON: {json}")

    def log_dict(self, dict):
        self.info(f"Dict: {dict}")

    def log_text(self, text):
        self.info(f"Text: {text}")
