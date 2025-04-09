from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import uvicorn

from core.models import Base, db_helper

from contextlib import asynccontextmanager

from items_views import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(items_router)


@app.get('/')
def hello_index():
    return {
        'message': 'Hello!',
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
