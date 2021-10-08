from os import environ


class Settings:
    debug = environ.get("DEBUG", "").lower() == "true"
