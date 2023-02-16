from fastapi import APIRouter

from .guild import user_guild_router
from .me import user_me_router

user_router = APIRouter(prefix='/user')
user_router.include_router(user_guild_router)
user_router.include_router(user_me_router)
