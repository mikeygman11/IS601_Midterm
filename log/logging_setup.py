# log/logging_setup.py
import logging
import os

def configure_logging(self):
    logging_conf_path = 'logging.conf'
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("logs/app.log"),  # Log to a file
                logging.StreamHandler()  # Also log to the console
            ]
        )
    logging.info("Logging configured successfully.")