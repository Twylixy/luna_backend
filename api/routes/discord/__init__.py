from fastapi import APIRouter

from .user import user_router

discord_router = APIRouter(prefix='/discord', tags=['discord'])
discord_router.include_router(user_router)
