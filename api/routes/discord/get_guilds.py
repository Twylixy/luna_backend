from typing import Union

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from api.database.crud import get_token_by_bearer, update_token
from api.database.engine import get_session
from api.helpers.discord import revoke_token_credentials
from api.responses.discord.get_guilds import GetGuildsResponse
from api.responses.error import ErrorResponse
from api.services.discord import get_user_guilds

router = APIRouter(prefix='/api/discord', tags=['discord'])
bearer_dependency = HTTPBearer(scheme_name='Bearer')


@router.get(
    '/get_guilds',
    response_model=GetGuildsResponse,
    responses={
        400: {'model': ErrorResponse},
    },
)
def get_guilds(
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[GetGuildsResponse, ErrorResponse]:
    """
    Fetch user's guilds from discord.

    Args:
      request: GetGuildsRequest
    Returns:
      Union[GetGuildsResponse, ErrorResponse]
    """
    token_object = get_token_by_bearer(session, bearer.credentials)

    if token_object is None:
        response = {
            'status': 'failure',
            'message': 'wrong token',
        }

        return ErrorResponse.parse_obj(response)

    success, guilds = get_user_guilds(token_object.access_token)

    if success is False:
        token_object = revoke_token_credentials(token_object)

        if token_object is None:
            response = {
                'status': 'failure',
                'message': 'token expired',
            }

            return ErrorResponse.parse_obj(response)

        token_object = update_token(
            session,
            token_object.discord_id,
            bearer.credentials,
            token_object.access_token,
            token_object.refresh_token,
        )

        success, guilds = get_user_guilds(token_object.access_token)

    response = {
        'status': 'success',
        'guilds': guilds,
    }

    return GetGuildsResponse.parse_obj(response)
