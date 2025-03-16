import logging
import logging.config
import os

def configure_logging(app_instance=None):
    """Configures logging using logging.conf to log only to a file."""
    log_directory = "logs"
    log_config_file = os.path.join(os.getcwd(), "log", "logging.conf")  # ✅ Correct path

    # Ensure logs directory exists
    os.makedirs(log_directory, exist_ok=True)

    if os.path.exists(log_config_file):
        logging.config.fileConfig(log_config_file, disable_existing_loggers=False)
    else:
        # Fallback if config file is missing
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Set logger for the App instance if provided
    if app_instance:
        app_instance.logger = logging.getLogger(__name__)