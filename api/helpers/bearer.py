import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from api.database.models import TokenModel
from api.entities.http import HTTPResponseCode
from api.services.discord import get_discord_user, refresh_oauth2_credentials


async def bearer_database_dependency(request: Request) -> HTTPAuthorizationCredentials:
    bearer = HTTPBearer(scheme_name='Bearer')
    bearer_credentials: Optional[HTTPAuthorizationCredentials]

    try:
        bearer_credentials = await bearer(request)
    except HTTPException as error:
        raise HTTPException(
            status_code=HTTPResponseCode.forbidden,
            detail='Not authenticated',
            headers={
                'WWW-Authenticate': 'Bearer',
            },
        )

    if bearer_credentials is None or bearer_credentials != os.getenv('DATABASE_API_KEY'):
        raise HTTPException(
            status_code=HTTPResponseCode.forbidden,
            detail='Not authenticated',
            headers={
                'WWW-Authenticate': 'Bearer',
            },
        )

    return bearer_credentials


async def exchange_bearer_to_token(session: Session, bearer: str) -> Optional[TokenModel]:
    """
    Return discord token by bearer, revoke if expire.

    Args:
        sessions: Session
        bearer: str
    Returns:
        Optional[TokenModel]
    """
    token_object: Optional[TokenModel] = (
        session.query(TokenModel).filter(TokenModel.bearer_token == bearer).first()
    )

    # implement null check for token_object because mypy doesn't understand that
    # sqlalchemy will return None if no object is found
    if token_object is None or token_object.access_token is None:
        return None

    user = await get_discord_user(token_object.access_token)

    # implement null check for user because mypy doesn't understand that
    # get_discord_user will return None if the access token is invalid
    if user is not None or token_object.refresh_token is None:
        return token_object

    oauth2_credentials = await refresh_oauth2_credentials(token_object.refresh_token)

    if oauth2_credentials is None:
        return None

    user = await get_discord_user(oauth2_credentials.access_token)

    if user is None:
        return None

    token_object.bearer_token = bearer
    token_object.access_token = oauth2_credentials.access_token
    token_object.refresh_token = oauth2_credentials.refresh_token
    token_object.expires = datetime.now() + timedelta(seconds=604800)

    return token_object
