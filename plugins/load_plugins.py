"""Loads all plugins automatically."""
import os
import importlib
import pkgutil
import logging

def load_plugins(command_handler):
    """Dynamically load and register plugins."""
    plugins_package = "plugins"
    plugins_path = os.path.join(os.getcwd(), "plugins")
    logger = logging.getLogger(__name__)
    
    logger.info("Loading plugins...")

    if not os.path.exists(plugins_path):
        logger.warning(f"Plugins directory '{plugins_path}' not found.")
        return

    for _, plugin_name, _ in pkgutil.iter_modules([plugins_path]):
        if plugin_name == "load_plugins":
            continue
        try:
            plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
            if hasattr(plugin_module, "register"):
                plugin_module.register(command_handler)
                logger.info(f"Plugin '{plugin_name}' registered successfully.")
            else:
                logger.warning(f"Plugin '{plugin_name}' does not have a register() function.")
        except ImportError as e:
            logger.error(f"Failed to load plugin '{plugin_name}': {e}")
