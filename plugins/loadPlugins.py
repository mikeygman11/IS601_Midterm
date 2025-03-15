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
