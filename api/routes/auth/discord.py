from datetime import datetime, timedelta
import os
import secrets
from typing import Union

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.database.engine import get_session
from api.database.models import TokenModel, UserModel
from api.entities.http import HTTPResponseCode
from api.requests.auth.discord import DiscordAuthRequest
from api.responses.auth.discord import DiscordAuthResponse
from api.responses.error import ErrorResponse
from api.services import discord

router = APIRouter(prefix='/api/auth', tags=['auth'])


@router.post(
    '/discord',
    response_model=DiscordAuthResponse,
    responses={
        HTTPResponseCode.bad_request: {'model': ErrorResponse},
    },
)
async def discord_auth(
    request: DiscordAuthRequest,
    session: Session = Depends(get_session),
) -> Union[DiscordAuthResponse, JSONResponse]:
    """
    Process discord oauth2 discord auth request.

    Args:
      request: DiscordAuthRequest
    Returns:
      Union[DiscordAuthResponse, ErrorResponse]
    """
    oauth2_credentials = await discord.get_oauth2_credentials(
        request.code,
        request.redirect_uri,
    )

    if oauth2_credentials is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='unable to get oauth2 credentials',
            ).dict(),
        )

    discord_user = await discord.get_discord_user(oauth2_credentials.access_token)

    if discord_user is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='unable to get user from discord',
            ).dict(),
        )

    user_object = (
        session.query(UserModel).filter(UserModel.discord_id == discord_user.id).first()
    )
    token_object = (
        session.query(TokenModel).filter(TokenModel.discord_id == discord_user.id).first()
    )
    bearer_token = secrets.token_hex(
        int(os.getenv('TOKEN_LENGTH', '32')),
    )

    if user_object is None:
        user_object = UserModel(discord_id=discord_user.id, email=discord_user.email)
        session.add(user_object)
        session.commit()
    else:
        user_object.email = discord_user.email
        session.refresh(user_object)

    if token_object is None:
        token_object = TokenModel(
            discord_id=discord_user.id,
            bearer_token=bearer_token,
            access_token=oauth2_credentials.access_token,
            refresh_token=oauth2_credentials.refresh_token,
        )
        session.add(token_object)
        session.commit()
    else:
        token_object.bearer_token = bearer_token
        token_object.access_token = oauth2_credentials.access_token
        token_object.refresh_token = oauth2_credentials.refresh_token
        token_object.expires = datetime.now() + timedelta(seconds=604800)
        session.refresh(token_object)

    return DiscordAuthResponse(
        status='success',
        token=token_object.bearer_token,
    )
