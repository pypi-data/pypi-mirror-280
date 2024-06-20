from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    partial_config_path: Path


settings = None


def init_settings(config_path: Path):
    global settings
    settings = Settings(partial_config_path=config_path)
    return settings


def get_settings():
    global settings
    return settings
