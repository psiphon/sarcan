from flask import Flask, request
from endpoints.voice import VoiceEndpoint
from endpoints.text import TextEndpoint
from personalities.glados import Glados
from config import Config
from logger import Logger

# init logger
logger = Logger("SARCAN")

glados = Glados()

# Initialize config
config = Config()
config.set_personality(glados)
config.set_logger(logger)

app = Flask(__name__)

# Initialize endpoint instances
text_endpoint = TextEndpoint(config)
voice_endpoint = VoiceEndpoint(config)

# Text endpoint route
@app.route('/text', methods=['POST'])
def text_input():
    return text_endpoint.process_request(request)

# Voice endpoint route
@app.route('/voice', methods=['POST'])
def voice_input():
    return voice_endpoint.process_request()

if __name__ == '__main__':
    app.run(debug=True)
