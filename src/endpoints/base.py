class BaseEndpoint:
    def __init__(self, config):
        self.config = config

    def process_request(self, accept_header):
        raise NotImplementedError()
    