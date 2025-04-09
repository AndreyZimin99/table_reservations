from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from sqlalchemy.orm import sessionmaker

from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str):
        self.engine = create_async_engine(
            url=url,
            echo=True
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(url=settings.DATABASE_URL)
