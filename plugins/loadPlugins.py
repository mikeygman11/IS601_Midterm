import importlib
import os
import pkgutil
import logging

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.logger = logging.getLogger(__name__)

    def load_plugins(self):
        """Dynamically loads available plugins."""
        plugin_dir = "plugins"
        if not os.path.exists(plugin_dir):
            os.makedirs(plugin_dir)
        for _, plugin_name, _ in pkgutil.iter_modules([plugin_dir]):
            try:
                module = importlib.import_module(f"plugins.{plugin_name}")
                self.plugins[plugin_name] = module
                self.logger.info(f"Loaded plugin: {plugin_name}")
                print(f"Plugin '{plugin_name}' loaded.")
            except Exception as e:
                self.logger.error(f"Failed to load plugin {plugin_name}: {e}")