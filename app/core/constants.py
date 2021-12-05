from pydantic import BaseModel


class Constants(BaseModel):
    """The app constants."""


constants = Constants()
