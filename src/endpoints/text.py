from endpoints.base import BaseEndpoint
from processors.text import TextProcessor
from config import Config

class TextEndpoint(BaseEndpoint):
    def __init__(self, config):
        super().__init__(config)

    def process_request(self, request):
        try:
            accept_header = request.headers["Accept"]

            # error check
            if request.get_data() is None:
                return self._return_error(accept_header)
            
            # ensure request is text
            # if "text/plain" not in request.headers["Content-Type"]:
            #     return self._return_error(accept_header)
            
            # ensure request is not empty
            if len(request.get_data()) < 5:
                return self._return_error(accept_header)
            
            #ensure request is not too long
            if len(request.get_data()) > Config().get_max_request_length():
                return self._return_error(accept_header)
            
            # Log request
            self.config.get_logger().log_request(request)
            input_text = request.get_data().decode("utf-8")
            self.config.get_logger().info(input_text)

            # Process text input
            answer = TextProcessor(self.config).process(input_text)

            # Log response
            self.config.get_logger().log_response(answer)

            return {"response": answer}
        except Exception as e:
            print(f"Error processing text input: {str(e)}")
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
