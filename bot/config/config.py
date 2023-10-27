from pydantic_settings import BaseSettings
import subprocess


class BotSettings(BaseSettings):
    token: str
    admin_ids: list[str]
    parse_mode: str


class Logging(BaseSettings):
    serialize: bool
    sink: str
    rotation: str
    compression: str
    format: str
    level: str


class DatabaseSettings(BaseSettings):
    drivername: str
    username: str
    password: str
    host: str
    port: int


class Settings(BaseSettings):
    bot: BotSettings
    logging: Logging
    # db: DatabaseSettings


config: Settings = Settings.parse_file(
    path="bot/config/settings.json",
    encoding="utf-8",
)
