from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Credentials(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    SECRET_KEY: str
    TOKEN: str
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_credentials():
    return Credentials()