from plugins import PluginManager
from processors.chatgpt import ChatGPT

# class TextProcessor takes input text and checks for a match against all plugins. 
# if matched the text is processed by that plugin
# if no plugins matched then the text is sent to chatgpt class
class TextProcessor:
    def __init__(self, config):
        self.plugins = PluginManager().plugins
        self.config = config

    def process(self, input_text):
        for plugin in self.plugins:
            if plugin.Plugin.match(input_text):
                return plugin.Plugin.process(input_text)
        return ChatGPT(self.config).process(input_text)


