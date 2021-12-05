from pydantic import BaseSettings


class Global(BaseSettings):
    """The app settings."""

    debug: bool = False

    class Config:
        """The Pydantic settings configuration."""

        env_file = ".env"


settings = Global()
