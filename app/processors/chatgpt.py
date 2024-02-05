from openai import OpenAI
from config import Config
import subprocess

import requests
import urllib.parse

# Set your OpenAI API key
class ChatGPT:
    def __init__(self, config):
        self.config = config
        self.client = OpenAI(api_key=config.get_openai_key())

    def process(self, question):
        # Call the OpenAI API to get the answer
        response = self.client.chat.completions.create(model="gpt-3.5-turbo", 
                    messages=[
                        {"role":"user","content":self.config.get_personality().get_chatgpt_instruction()},
                        {"role":"user","content":"try to keep responses below the character count " + str(self.config.get_max_request_length())},
                        {"role":"user","content":question.strip()}
                    ],
                    max_tokens=100)
        # if response.choices length is 0 then throw an error
        if len(response.choices) == 0:
            raise Exception("No response from OpenAI")
        
        # Print the answer
        answer = response.choices[0].message.content.strip()
        
        # log the answer
        print("ChatGPT:", answer)
        return answer


