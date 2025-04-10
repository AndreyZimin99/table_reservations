from fastapi import APIRouter

from .tables.views import router as tables_router
from .reservations.views import router as reservations_router

router = APIRouter()
router.include_router(router=tables_router, prefix='/tables')
router.include_router(router=reservations_router, prefix='/reservations')
