from typing import Union

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from api.database.engine import get_session
from api.entities.http import HTTPResponseCode
from api.helpers.bearer import exchange_bearer_to_token
from api.responses.discord.get_guild import GetGuildResponse
from api.responses.discord.get_guilds import GetGuildsResponse
from api.responses.error import ErrorResponse
from api.services.discord import get_user_guilds

user_guild_router = APIRouter()
bearer_dependency = HTTPBearer(scheme_name='Bearer')


@user_guild_router.get(
    '/guild',
    response_model=GetGuildsResponse,
    responses={
        HTTPResponseCode.bad_request: {'model': ErrorResponse},
    },
)
async def get_guilds(
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[GetGuildsResponse, JSONResponse]:
    """
    Fetch user's guilds from discord.

    Args:
      request: GetGuildsRequest
    Returns:
      Union[GetGuildsResponse, ErrorResponse]
    """
    token_object = await exchange_bearer_to_token(session, bearer.credentials)

    # implement null check for token_object because mypy doesn't understand that
    # sqlalchemy will return None if no object is found
    if token_object is None or token_object.access_token is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='missing token',
            ).dict(),
        )

    guilds = await get_user_guilds(token_object.access_token)

    return GetGuildsResponse(
        status='success',
        guilds=guilds,
    )


@user_guild_router.get(
    '/guild/{guild_id}',
    response_model=GetGuildResponse,
    responses={
        HTTPResponseCode.bad_request: {'model': ErrorResponse},
        HTTPResponseCode.unauthorized: {'model': ErrorResponse},
    },
)
async def get_guild(
    guild_id: int,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[GetGuildResponse, JSONResponse]:
    """
    Return guild from discord.

    Args:
        bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
        session: Session = Depends(get_session),
    Returns:
        Union[GetGuildResponse, ErrorResponse]
    """
    token_object = await exchange_bearer_to_token(session, bearer.credentials)

    # implement null check for token_object because mypy doesn't understand that
    # sqlalchemy will return None if no object is found
    if token_object is None or token_object.access_token is None:
        return JSONResponse(
            status_code=HTTPResponseCode.unauthorized,
            content=ErrorResponse(
                status='failure',
                message='valid bearer token required',
            ).dict(),
        )

    guilds = await get_user_guilds(token_object.access_token)
    selected_guild = None

    if guilds is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='unable to fetch guilds from Discord',
            ).dict(),
        )

    for guild in guilds:
        if guild.id == guild_id:
            selected_guild = guild
            break

    if selected_guild is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='guild not found',
            ).dict(),
        )

    return GetGuildResponse(
        status='success',
        guild=selected_guild,
    )
