"""loading all the plugins automatically"""
import importlib
import os
import pkgutil
import logging

def load_plugins(command_handler):
    """Loading all the calculation plugins automatically."""
    plugins_package = "plugins"
    plugins_path = os.path.join(os.getcwd(), "plugins")
    logger = logging.getLogger(__name__)
    logger.info("Loading plugins...")

    if not os.path.exists(plugins_path):
        logger.warning("Plugins directory '%s' not found.", plugins_path)
        return

    for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
        if plugin_name == "load_plugins" or is_pkg:
            continue

        try:
            plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
            if hasattr(plugin_module, "register"):
                plugin_module.register(command_handler)
                logger.info("Plugin '%s' loaded successfully.", plugin_name)
            else:
                logger.warning("Plugin '%s' does not have a register() function.", plugin_name)

        except ImportError as e:
            logger.error("Failed to load plugin '%s': %s", plugin_name, e)
