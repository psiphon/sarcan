# config class for the project
# sets the assistant personality
# sets the assistant name
# sets the assistant voice
# sets the verbosity of output
# sets the log file
# sets the log level
# sets the log format

# Path: src/config.py
# Compare this snippet from src/config.py:


class Config:
    def __init__(self):
        self.personality = None
        self.logger = None
        self.tmp_dir = "/tmp"
        self.glados_server = "http://localhost:8124"
        self.max_request_length = 300

    def set_personality(self, personality):
        self.personality = personality
    
    def get_personality(self):
        return self.personality
    
    def get_tmp_dir(self):
        return self.tmp_dir
    
    def get_glados_server(self):
        return self.glados_server
    
    def get_max_request_length(self):
        return self.max_request_length
    
    def set_logger(self, logger):
        self.logger = logger

    def get_logger(self):
        return self.logger
        