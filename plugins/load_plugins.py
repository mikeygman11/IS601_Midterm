import importlib
import os
import pkgutil
import logging

def load_plugins(command_handler):
    plugins_package = "plugins"
    plugins_path = os.path.join(os.getcwd(), "plugins")
    logger = logging.getLogger(__name__)
    logger.info("Loading plugins...")
    if not os.path.exists(plugins_path):
        logger.warning(f"Plugins directory '{plugins_path}' not found.")
        print(f"WARNING: Plugins directory '{plugins_path}' not found.")
        return
    print("DEBUG: Loading plugins...")
    for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
        if plugin_name == "load_plugins" or is_pkg:
            continue  # Skip the plugin loader and any package directories
        try:
            plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
            print(f"DEBUG: Found plugin '{plugin_name}'")

            if hasattr(plugin_module, "register"):
                plugin_module.register(command_handler)  # ✅ Use `command_handler` directly (No `self.`)
                logger.info(f"Plugin '{plugin_name}' loaded successfully.")
                print(f"DEBUG: Plugin '{plugin_name}' registered successfully!")
            else:
                logger.warning(f"Plugin '{plugin_name}' does not have a register() function.")
                print(f"WARNING: Plugin '{plugin_name}' does not have a register() function.")
        except ImportError as e:
            logger.error(f"Failed to load plugin '{plugin_name}': {e}")
            print(f"ERROR: Failed to load plugin '{plugin_name}': {e}")
