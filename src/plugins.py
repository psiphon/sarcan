import os
import importlib.util

class PluginManager:
    def __init__(self):
        self.plugins = self.load_plugins()

    def load_plugins(self):
        # Load plugins dynamically from the plugins folder
        plugins = []
        plugins_dir = os.path.join(os.path.dirname(__file__), "plugins")
        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = os.path.splitext(filename)[0]
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(plugins_dir, filename))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                plugins.append(module)
        return plugins

