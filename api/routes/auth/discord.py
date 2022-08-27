import os
import secrets
from typing import Union

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.database.crud import (
    create_token,
    create_user,
    get_token_by_discord_id,
    get_user_by_discord_id,
    update_token,
    update_user,
)
from api.database.engine import get_session
from api.entities.http import HTTPResponseCode
from api.requests.auth.discord import DiscordAuthRequest
from api.responses.auth.discord import DiscordAuthResponse
from api.responses.error import ErrorResponse
from api.services.discord import get_discord_user, get_oauth2_credentials

router = APIRouter(prefix='/api/auth', tags=['auth'])


@router.post(
    '/discord',
    response_model=DiscordAuthResponse,
    responses={
        HTTPResponseCode.bad_request: {'model': ErrorResponse},
    },
)
def discord_auth(
    request: DiscordAuthRequest,
    session: Session = Depends(get_session),
) -> Union[DiscordAuthResponse, ErrorResponse]:
    """
    Process discord oauth2 discord auth request.

    Args:
      request: DiscordAuthRequest
    Returns:
      Union[DiscordAuthResponse, ErrorResponse]
    """
    oauth2_credentials = get_oauth2_credentials(
        request.code,
        request.redirect_uri,
    )

    if oauth2_credentials is None:
        response = {
            'status': 'failure',
            'message': 'unable to get oauth2 credentials',
        }

        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse.parse_obj(response).dict(),
        )

    discord_user = get_discord_user(oauth2_credentials.access_token)

    if discord_user is None:
        response = {
            'status': 'failure',
            'message': 'unable to get user from discord',
        }

        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse.parse_obj(response).dict(),
        )

    user_object = get_user_by_discord_id(session, discord_user.id)
    token_object = get_token_by_discord_id(session, discord_user.id)
    bearer_token = secrets.token_hex(
        int(os.getenv('TOKEN_LENGTH', '32')),
    )

    if user_object is None:
        user_object = create_user(
            session,
            discord_user.id,
            discord_user.email,
        )
    else:
        update_user(
            session,
            user_object.id,
            user_object.email,
        )

    if token_object is None:
        token_object = create_token(
            session,
            discord_user.id,
            bearer_token,
            oauth2_credentials.access_token,
            oauth2_credentials.refresh_token,
        )
    else:
        update_token(
            session,
            user_object.id,
            bearer_token,
            oauth2_credentials.access_token,
            oauth2_credentials.refresh_token,
        )

    response = {
        'status': 'success',
        'token': token_object.bearer_token,
    }

    return DiscordAuthResponse.parse_obj(response).dict()
