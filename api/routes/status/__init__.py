from fastapi import APIRouter

from .healthcheck import healthcheck_router

status_router = APIRouter(prefix='/status', tags=['status'])
status_router.include_router(healthcheck_router)
