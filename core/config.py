from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_v1_prefix: str = '/api/v1'

    POSTGRES_HOST: str = 'db'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'postgres'
    POSTGRES_USER: str = 'user'
    POSTGRES_PASSWORD: str = '1234'

    @property
    def DATABASE_URL(self):
        return (
            f'postgresql+asyncpg://{self.POSTGRES_USER}:'
            f'{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:'
            f'{self.POSTGRES_PORT}/{self.POSTGRES_DB}'
        )

    # model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
