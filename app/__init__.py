try:
    from dotenv import load_dotenv

    load_dotenv()
except ModuleNotFoundError:
    pass

import logging.handlers
import os
from datetime import datetime
from pathlib import Path

from app.config import Settings

# Set up file logging
log_dir = Path("app/logs")
log_file = log_dir / f"{datetime.today().strftime('%d-%m-%Y')}.log"
os.makedirs(log_dir, exist_ok=True)

# File handler rotates logs every 5 MB
file_handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=5 * (2 ** 20), backupCount=10, encoding="utf-8",
)
file_handler.setLevel(logging.DEBUG)

# Console handler prints to terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG if Settings.debug else logging.INFO)

# Add colors for logging if available.
try:
    from colorlog import ColoredFormatter

    console_handler.setFormatter(
        ColoredFormatter(fmt="%(log_color)s%(asctime)s - %(name)s %(levelname)s: %(message)s", datefmt="%D %H:%M:%S"))
except ModuleNotFoundError:
    pass

# Remove old loggers, if any
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)

# Silence irrelevant loggers
logging.getLogger("").setLevel(logging.ERROR)

# Setup new logging configuration
logging.basicConfig(
    format="%(asctime)s - %(name)s %(levelname)s: %(message)s",
    datefmt="%D %H:%M:%S",
    level=logging.DEBUG,
    handlers=[console_handler, file_handler]
)

log = logging.getLogger()

log.debug("Logging initialization complete")
