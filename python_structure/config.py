from datetime import datetime
from os import environ
from pathlib import Path


class Settings:
    debug = environ.get("DEBUG", "").lower() == "true"


class Logs:
    path = Path("python_structure/logs")
    name = f"{datetime.today().strftime('%d-%m-%Y')}.log"

    fmt = "%(asctime)s - %(name)s %(levelname)s: %(message)s"
    datefmt = "%D %H:%M:%S"
