from endpoints.base import BaseEndpoint

class VoiceEndpoint(BaseEndpoint):
    def __init__(self, config):
        super().__init__(config)
        
    def process_request(self, accept_header):
        try:
            # Process voice input request
            return {"response": "Processed voice input"}
        except Exception as e:
            print(f"Error processing voice input: {str(e)}")
            return self._return_error(accept_header)

    def _return_error(self, accept_header):
        if "audio/wav" in accept_header:
            # Return error WAV file
            with open("error.wav", "rb") as f:
                error_wav = f.read()
            return error_wav, 500  # HTTP status code 500 for internal server error
        else:
            # Return error text
            return {"error": "Internal server error"}, 500
