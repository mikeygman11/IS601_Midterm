import logging
import logging.config
import os
from dotenv import load_dotenv

def configure_logging(app_instance=None):
    """Configures logging dynamically using environment variables."""
    load_dotenv()
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="logs/app.log",
        filemode="a"
    )

    if app_instance:
        app_instance.logger = logging.getLogger(__name__)