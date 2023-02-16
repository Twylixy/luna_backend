from typing import Union

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from api.database.engine import get_session
from api.entities.http import HTTPResponseCode
from api.helpers.bearer import exchange_bearer_to_token
from api.responses.discord.get_me import GetMeResponse
from api.responses.error import ErrorResponse
from api.services.discord import get_discord_user

user_me_router = APIRouter()
bearer_dependency = HTTPBearer(scheme_name='Bearer')


@user_me_router.get(
    '/me',
    response_model=GetMeResponse,
    responses={
        HTTPResponseCode.bad_request: {'model': ErrorResponse},
    },
)
async def get_guilds(
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[GetMeResponse, JSONResponse]:
    """
    Return Discord user.

    Args:
      request: GetGuildsRequest
    Returns:
      Union[GetMeResponse, ErrorResponse]
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

    user = await get_discord_user(token_object.access_token)

    return GetMeResponse(
        status='success',
        user=user,
    )
