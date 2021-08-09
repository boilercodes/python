try:
    from dotenv import load_dotenv

    load_dotenv()
except ModuleNotFoundError:
    pass

import logging.handlers
import os

from python_structure.config import Logs, Settings

# Configure the "TRACE" logging level (e.g. "log.trace(message)")
logging.TRACE = 5
logging.addLevelName(logging.TRACE, "TRACE")


def monkeypatch_trace(self: logging.Logger, msg: str, *args, **kwargs) -> None:
    """
    Log 'msg % args' with severity 'TRACE'.

    To pass exception information, use the keyword argument exc_info with a true value, e.g.
    logger.trace("Houston, we have an %s", "interesting problem", exc_info=1)
    """
    if self.isEnabledFor(logging.TRACE):
        self._log(logging.TRACE, msg, args, **kwargs)


logging.Logger.trace = monkeypatch_trace

# Set up file logging
log_file = Logs.path / Logs.name
os.makedirs(Logs.path, exist_ok=True)

# File handler rotates logs every 5 MB
file_handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=5 * (2 ** 20), backupCount=10, encoding="utf-8",
)
file_handler.setLevel(logging.TRACE if Settings.debug else logging.DEBUG)

# Console handler prints to terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.TRACE if Settings.debug else logging.INFO)

# Add colors for logging if available.
try:
    from colorlog import ColoredFormatter

    console_handler.setFormatter(
        ColoredFormatter(fmt=f"%(log_color)s{Logs.fmt}", datefmt=Logs.datefmt))
except ModuleNotFoundError:
    pass

# Remove old loggers, if any
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)

# Silence irrelevant loggers
logging.getLogger("discord").setLevel(logging.ERROR)
logging.getLogger("discord_slash").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.ERROR)

# Setup new logging configuration
logging.basicConfig(format=Logs.fmt,
                    datefmt=Logs.datefmt,
                    level=logging.DEBUG,
                    handlers=[console_handler, file_handler])

log = logging.getLogger()

log.debug("Logging initialization complete")
