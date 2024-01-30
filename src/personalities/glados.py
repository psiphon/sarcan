import subprocess 
import requests
import urllib.parse
from config import Config

class Glados:
    def get_chatgpt_instruction(self):
        return "responses should be in the style of glados from portal game"
    
    def text_to_voice(text):
        # Encode the answer
        encoded_answer = urllib.parse.quote(text)

        # Send the encoded answer as a query param to localhost:1234/synthesize/ and save the resulting binary response to /tmp/output.wav
        url = Config.get_glados_server() + f"/synthesize/?text={encoded_answer}"
        r = requests.get(url)

        # if the response is not 200 then throw an error
        if r.status_code != 200:
            raise Exception("Error from Glados TTS server. Status code: " + str(r.status_code))

        with open('/tmp/output.wav', 'wb') as f:
            f.write(r.content)

        return '/tmp/output.wav'

        