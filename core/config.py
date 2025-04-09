# POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
# POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
# POSTGRES_DB = os.environ.get("POSTGRES_DB", "sciarticle_db")
# POSTGRES_USER = os.environ.get("POSTGRES_USER", "user")
# POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")
# DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def DATABASE_URL(self):
        return (
            f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@'
            f'{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'
        )

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
