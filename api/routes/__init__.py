from fastapi import APIRouter

from .database import database_router
from .discord import discord_router
from .oauth2 import oauth2_router
from .status import status_router

api_router = APIRouter(prefix='/api')
api_router.include_router(database_router)
api_router.include_router(discord_router)
api_router.include_router(oauth2_router)
api_router.include_router(status_router)
