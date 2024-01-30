from openai import OpenAI
from config import Config
import subprocess

client = OpenAI(api_key='s...kLT')
import requests
import urllib.parse

# Set your OpenAI API key
class ChatGPT:
    def __init__(self, config):
        self.config = config

    def process(self, question):
        # Call the OpenAI API to get the answer
        response = client.chat.completions.create(model="gpt-3.5-turbo", 
                    messages=[
                        {"role":"user","content":self.config.get_personality().get_chatgpt_instruction()},
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


