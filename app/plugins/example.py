class Plugin() :
    @staticmethod
    def match(config, input_text):
        return input_text.lower().startswith("hello world")

    @staticmethod
    def process(config, input_text):
        # Example result text for plugin 1
        return "Plugin 1 matched!"
