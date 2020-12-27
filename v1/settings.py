from pydantic import BaseSettings


class Settings(BaseSettings):
    FIREB_API_KEY: str
    PROJECT_ID: str = "Local"
    SHORT_SHA: str = "local"
