import os
import json

class Config:
    def __init__(self):
        self.personality = None
        self.personality_name = "glados"
        self.logger = None
        self.tmp_dir = "/tmp"
        self.audio_dir = "static/audio"
        self.glados_server = "http://localhost:8124"
        self.max_request_length = 300
        self.openai_key = None
        self.homeassistant_url = "http://localhost:8123"
        self.homeassistant_token = None
        self.read_config(self.find_config_file())
        self.read_config_from_env()
        if self.openai_key is None:
            raise Exception("OpenAI key not found. Please set OPENAI_KEY environment variable or add to config.json file")
        if self.personality_name is None:
            raise Exception("Personality not found. Please set PERSONALITY environment variable or add to config.json file")

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
        if "homeassistantUrl" in config:
            self.homeassistant_url = config["homeassistantUrl"]
        if "homeassistantToken" in config:
            self.homeassistant_token = config["homeassistantToken"]

    def find_config_file(self):
        config_file = "config.json"
        if os.path.exists(config_file):
            return config_file
        config_file = os.path.join(os.path.dirname(__file__), "..", "config", "config.json")
        if os.path.exists(config_file):
            return config_file
        config_file = os.path.join(os.path.dirname(__file__), "..", "config.json")
        if os.path.exists(config_file):
            return config_file
        raise Exception("Could not find config.json file")
    
    def read_config_from_env(self):
        if "SARCAN_PERSONALITY" in os.environ:
            self.personality_name = os.environ["SARCAN_PERSONALITY"]
        if "SARCAN_TMP_DIR" in os.environ:
            self.tmp_dir = os.environ["SARCAN_TMP_DIR"]
        if "SARCAN_GLADOS_SERVER_URL" in os.environ:
            self.glados_server = os.environ["SARCAN_GLADOS_SERVER_URL"]
        if "SARCAN_MAX_REQUEST_LENGTH" in os.environ:
            self.max_request_length = os.environ["SARCAN_MAX_REQUEST_LENGTH"]
        if "SARCAN_OPENAI_KEY" in os.environ:
            self.openai_key = os.environ["SARCAN_OPENAI_KEY"]
        if "SARCAN_HOMEASSISTANT_URL" in os.environ:
            self.homeassistant_url = os.environ["SARCAN_HOMEASSISTANT_URL"]
        if "SARCAN_HOMEASSISTANT_TOKEN" in os.environ:
            self.homeassistant_token = os.environ["SARCAN_HOMEASSISTANT_TOKEN"]

    def set_personality(self, personality):
        self.personality = personality
    
    def get_personality_name(self):
        return self.personality_name
    
    def get_personality(self):
        return self.personality
    
    def get_tmp_dir(self):
        return self.tmp_dir
    
    def set_audio_dir(self, audio_dir):
        self.audio_dir = audio_dir
    
    def get_audio_dir(self):
        return self.audio_dir
    
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

    def get_homeassistant_url(self):
        return self.homeassistant_url
    
    def get_homeassistant_token(self):
        return self.homeassistant_token
        