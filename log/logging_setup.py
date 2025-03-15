# log/logging_setup.py
import logging
import os

def configure_logging():
    """Set up logging configuration."""
    print("DEBUG: configure_logging() function called.")  # Debug print statement

    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.getenv("LOG_FILE", os.path.join(log_dir, "app.log"))
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    print(f"DEBUG: Logging to {os.path.abspath(log_file)}")  # Debug print statement

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Also log to console
        ]
    )

    logging.info("Logging system initialized.")  # Log an initial message