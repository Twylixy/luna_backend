from fastapi import APIRouter

from .guild import database_guild_crud_router
from .user import database_user_crud_router

database_router = APIRouter(prefix='/database', tags=['database'])
database_router.include_router(database_guild_crud_router)
database_router.include_router(database_user_crud_router)
