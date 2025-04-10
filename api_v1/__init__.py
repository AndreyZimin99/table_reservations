from fastapi import APIRouter

from .tables.views import router as tables_router

router = APIRouter()
router.include_router(router=tables_router, prefix='/tables')
