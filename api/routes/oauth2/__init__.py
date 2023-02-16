from fastapi import APIRouter

from .discord import discord_auth_router

oauth2_router = APIRouter(prefix='/oauth2', tags=['oauth2'])
oauth2_router.include_router(discord_auth_router)
