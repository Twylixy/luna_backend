from typing import Union

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from api.database.engine import get_session
from api.entities.http import HTTPResponseCode
from api.helpers.bearer import exchange_bearer_to_token
from api.responses.discord.get_guilds import GetGuildsResponse
from api.responses.error import ErrorResponse
from api.services.discord import get_user_guilds

router = APIRouter(prefix='/api/discord', tags=['discord'])
bearer_dependency = HTTPBearer(scheme_name='Bearer')


@router.get(
    '/get_guilds',
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
