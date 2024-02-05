from flask import Flask, request, send_from_directory
from endpoints.voice import VoiceEndpoint
from endpoints.text import TextEndpoint
from personalities.glados import Glados
from config import Config
from logger import Logger

# init logger
logger = Logger("SARCAN")

# Initialize config
config = Config()
config.set_logger(logger)
config.set_audio_dir("static/audio")

if config.get_personality_name() == "glados":
    glados = Glados(config)
    config.set_personality(glados)
else:
    raise Exception("Invalid personality")

app = Flask(__name__)
app.static_folder = 'static'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# Initialize endpoint instances
text_endpoint = TextEndpoint(config)
voice_endpoint = VoiceEndpoint(config)

# Text endpoint route
@app.route('/api/text', methods=['POST'])
def text_input():
    return text_endpoint.process_request(request)

# Voice endpoint route
@app.route('/api/voice', methods=['POST'])
def voice_input():
    return voice_endpoint.process_request()

# serve the wav file
@app.route('/audio/<path:path>')
def send_wav(path):
    return send_from_directory(config.get_audio_dir(), path)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
