import os
import json

class Config:
    def __init__(self):
        self.personality = None
        self.personality_name = "glados"
        self.logger = None
        self.tmp_dir = "/tmp"
        self.glados_server = "http://localhost:8124"
        self.max_request_length = 300
        self.openai_key = "sk-"
        self.read_config(self.find_config_file())

    def read_config(self, config_file):
        with open(config_file) as f:
            config = json.load(f)
            if self.validate_config(config):
                self._set_config(config)

    def validate_config(self, config):
        if "personality" in config:
            if config["personality"] not in ["glados"]:
                raise Exception("Invalid personality")
        if "gladosServerUrl" in config:
            # ensure a valid URL is provided
            if not config["gladosServerUrl"].startswith("http"):
                raise Exception("Invalid gladosServerUrl")
        if "openAiKey" not in config:
            raise Exception("Invalid openAiKey")
        return True

    def _set_config(self, config):
        if "personality" in config:
            self.personality_name = config["personality"]
        if "tmpDir" in config:
            self.tmp_dir = config["tmpDir"]
        if "gladosServerUrl" in config:
            self.glados_server = config["gladosServerUrl"]
        if "maxRequestLength" in config:
            self.max_request_length = config["maxRequestLength"]
        if "openAiKey" in config:
            self.openai_key = config["openAiKey"]

    def find_config_file(self):
        config_file = "config.json"
        if os.path.exists(config_file):
            return config_file
        config_file = os.path.join(os.path.dirname(__file__), "config", "config.json")
        if os.path.exists(config_file):
            return config_file
        config_file = os.path.join(os.path.dirname(__file__), "..", "config.json")
        if os.path.exists(config_file):
            return config_file
        raise Exception("Could not find config.json file")

    def set_personality(self, personality):
        self.personality = personality
    
    def get_personality_name(self):
        return self.personality_name
    
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
    
    def get_openai_key(self):
        return self.openai_key
        