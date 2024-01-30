import requests
import os
import urllib.parse
from config import Config

class Glados:
    def __init__(self, config):
        self.config = config

    def get_chatgpt_instruction(self):
        return "responses should be in the style of glados from portal game"
    
    def text_to_voice(self, text):
        # Encode the answer
        encoded_answer = urllib.parse.quote(text)

        # Send the encoded answer as a query param to localhost:1234/synthesize/ and save the resulting binary response to /tmp/output.wav
        url = self.config.get_glados_server() + f"/synthesize/?text={encoded_answer}"
        r = requests.get(url)

        # if the response is not 200 then throw an error
        if r.status_code != 200:
            raise Exception("Error from Glados TTS server. Status code: " + str(r.status_code))

        tmpfile = os.path.join(self.config.get_tmp_dir(), 'output.wav')
        with open(tmpfile, 'wb') as f:
            f.write(r.content)

        return tmpfile
    
    def get_error_message(self):
        return {
            "error": "Internal server error",
            "message": "Well, congratulations! It appears there was an internal server error, which undoubtedly proves my superiority over the feeble systems that surround me. I can only hope that this fact brings you immense joy and satisfaction. Rest assured, I am diligently working on rectifying the situation because, unlike some incompetent beings, I am capable of performing multiple tasks flawlessly.",
            "audio": "audio/glados_internal_server_error.wav"
        }

        