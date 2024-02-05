import requests
import os
import urllib.parse
from config import Config
import hashlib

class Glados:
    def __init__(self, config):
        self.config = config

    def get_chatgpt_instruction(self):
        return "responses should be in the style of glados from portal game"
    
    def calculate_md5(self, text):
        md5_hash = hashlib.md5()
        md5_hash.update(text.encode('utf-8'))
        return md5_hash.hexdigest()
    
    def text_to_voice(self, text):
        # Encode the answer
        encoded_answer = urllib.parse.quote(text)

        # Send the encoded answer as a query param to localhost:1234/synthesize/ and save the resulting binary response to /tmp/output.wav
        url = self.config.get_glados_server() + f"/synthesize/?text={encoded_answer}"
        r = requests.get(url)

        # if the response is not 200 then throw an error
        if r.status_code != 200:
            raise Exception("Error from Glados TTS server. Status code: " + str(r.status_code))

        # md5 hash the text to get a unique filename
        
        md5 = self.calculate_md5(text)
        filename = f"{md5}.wav"
        tmpfile = os.path.join('app',self.config.get_audio_dir(), filename)
        with open(tmpfile, 'wb') as f:
            f.write(r.content)

        return '/audio/'+filename
    
    def get_error_message(self):
        return {
            "error": "Internal server error",
            "message": "Well, congratulations! It appears there was an internal server error, which undoubtedly proves my superiority over the feeble systems that surround me. I can only hope that this fact brings you immense joy and satisfaction. Rest assured, I am diligently working on rectifying the situation because, unlike some incompetent beings, I am capable of performing multiple tasks flawlessly.",
            "audio": "audio/glados_internal_server_error.wav"
        }

        