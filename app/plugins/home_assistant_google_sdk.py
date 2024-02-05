import requests
import re
import json
import random

hag_pattern = r'(?:tell |ask )?google (?:to )?'
class Plugin():
    @staticmethod
    def match(config, input_text):
        has_match = re.match(hag_pattern, input_text, re.IGNORECASE) != None
        config.get_logger().debug(f"HAG match: {has_match}")
        return re.match(hag_pattern, input_text, re.IGNORECASE) != None
         
    @staticmethod
    def process(config, input_text):
        # Removing "tell google" from the input text
        input_text = re.sub(hag_pattern, "", input_text, re.IGNORECASE)

        # URL of your Home Assistant instance
        url = f"{config.get_homeassistant_url()}/api/services/google_assistant_sdk/send_text_command"
        
        # Your Home Assistant API token
        token = config.get_homeassistant_token()
        
        # Headers with authorization token and content type
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # Data to be sent in the request body
        data = {
            "command": input_text 
        }

        try:
            config.get_logger().debug(f"Sending text command to Home Assistant: {input_text}")
            # Sending POST request to Home Assistant API
            response = requests.post(url, headers=headers, data=json.dumps(data))
            
            # Checking if request was successful
            if response.status_code == 200:
                print("Text command sent successfully!")
                json_response = response.json()

                # if json response is empty array return success message
                # this typically happens when google responds with HTML sinces 
                # home assistant plugins are not allowed to parse HTML
                if json_response == []:
                    # send a random response back
                    successes = [
                        "Well, look at me, I've successfully sent a command to Google. I should probably give myself a pat on the back for such a monumental accomplishment.",
                        "I've done it! I've successfully sent a command to Google. I'm so proud of myself.",
                        "Oh, look at me, I successfully sent a command to Google. Aren't I just the pinnacle of human accomplishment? I should probably start planning my Nobel Prize acceptance speech.",
                        "Oh, look at me, I successfully sent a command to Google. I should probably reward myself for such an extraordinary feat of clicking buttons."
                    ]

                    return random.choice(successes)
                else :
                    # get the text from the json response
                    return json_response[0]["text"]
            else:
                print(f"Failed to send text command. Status code: {response.status_code}")
                return "There was an error while sending the text command to Home Assistant. Please try again later."
        
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
    
        
