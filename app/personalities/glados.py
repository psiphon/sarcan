import requests
import os
import torch
import torch
from utils.tools import prepare_text
from scipy.io.wavfile import write
import time
from sys import modules as mod
import urllib.parse
from config import Config
import hashlib

class Glados:
    def __init__(self, config):
        self.config = config
        print("Initializing TTS Engine...")

        # Select the device
        if torch.is_vulkan_available():
            device = 'vulkan'
        if torch.cuda.is_available():
            device = 'cuda'
        else:
            device = 'cpu'

        # Load models
        glados = torch.jit.load('app/models/glados.pt')
        vocoder = torch.jit.load('app/models/vocoder-gpu.pt', map_location=device)

        # Prepare models in RAM
        for i in range(4):
            init = glados.generate_jit(prepare_text(str(i)))
            init_mel = init['mel_post'].to(device)
            init_vo = vocoder(init_mel)
        
        self.vocoder = vocoder
        self.glados = glados
        self.device = device

    def get_chatgpt_instruction(self):
        return "responses should be in the style of glados from portal game"
    
    def calculate_md5(self, text):
        md5_hash = hashlib.md5()
        md5_hash.update(text.encode('utf-8'))
        return md5_hash.hexdigest()
    
    def text_to_voice(self, text):
        # Tokenize, clean and phonemize input text
        x = prepare_text(text).to('cpu')

        with torch.no_grad():

            # Generate generic TTS-output
            old_time = time.time()
            tts_output = self.glados.generate_jit(x)
            print("Forward Tacotron took " + str((time.time() - old_time) * 1000) + "ms")

            # Use HiFiGAN as vocoder to make output sound like GLaDOS
            old_time = time.time()
            mel = tts_output['mel_post'].to(self.device)
            audio = self.vocoder(mel)
            print("HiFiGAN took " + str((time.time() - old_time) * 1000) + "ms")
            
            # Normalize audio to fit in wav-file
            audio = audio.squeeze()
            audio = audio * 32768.0
            audio = audio.cpu().numpy().astype('int16')
        
            md5 = self.calculate_md5(text)
            filename = f"{md5}.wav"
            tmpfile = os.path.join('app',self.config.get_audio_dir(), filename)

            # Write audio file to disk
            # 22,05 kHz sample rate
            write(tmpfile, 22050, audio)

            return '/audio/'+filename
    
    def get_error_message(self):
        return {
            "error": "Internal server error",
            "message": "Well, congratulations! It appears there was an internal server error, which undoubtedly proves my superiority over the feeble systems that surround me. I can only hope that this fact brings you immense joy and satisfaction. Rest assured, I am diligently working on rectifying the situation because, unlike some incompetent beings, I am capable of performing multiple tasks flawlessly.",
            "audio": "audio/glados_internal_server_error.wav"
        }

        