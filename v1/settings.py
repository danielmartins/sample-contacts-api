from pydantic import BaseSettings


class Settings(BaseSettings):
    FIREB_API_KEY: str
