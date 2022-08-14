import os
from typing import Optional

import requests
from pydantic import BaseModel


class OAuth2Credentials(BaseModel):
    """Represents oauth2 credentials."""

    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str


class DiscordUser(BaseModel):
    """Represents discord user."""

    id: int
    username: str
    email: str


def get_oauth2_credentials(
    discord_code: str,
    redirect_uri: str,
) -> Optional[OAuth2Credentials]:
    """
    Get oauth2 credentials from discord.

    Args:
        discord_code: str
    Returns:
        Optional[OAuth2Credentials]
    """
    oauth2_request = requests.post(
        '{0}/oauth2/token'.format(
            os.getenv('DISCORD_ENDPOINT'),
        ),
        data={
            'client_id': os.getenv('CLIENT_ID'),
            'client_secret': os.getenv('CLIENT_SECRET'),
            'grant_type': 'authorization_code',
            'code': discord_code,
            'redirect_uri': redirect_uri,
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    )

    try:
        oauth2_request.raise_for_status()
    except requests.HTTPError:
        return None

    return OAuth2Credentials(**oauth2_request.json())


def get_discord_user(access_token: str) -> Optional[DiscordUser]:
    """
    Get user from discord.

    Args:
        access_token: str
    Returns:
        Optional[DiscordUser]
    """
    get_user_request = requests.get(
        '{0}/users/@me'.format(
            os.getenv('DISCORD_ENDPOINT'),
        ),
        headers={
            'Authorization': 'Bearer {0}'.format(
                access_token,
            ),
        },
    )

    try:
        get_user_request.raise_for_status()
    except requests.HTTPError:
        return None

    return DiscordUser(**get_user_request.json())
