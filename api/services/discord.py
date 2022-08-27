import os
from typing import List, Optional, Tuple

import requests

from api.entities.discord import (
    DiscordServer,
    DiscordUser,
    OAuth2TokenCredentials,
)


class DiscordPermission:
    """Represents Discord permissions."""

    administrator = 0x80


def get_oauth2_credentials(
    discord_code: str,
    redirect_uri: str,
) -> Optional[OAuth2TokenCredentials]:
    """
    Get oauth2 credentials from discord.

    Args:
        discord_code: str
        redirect_uri: str
    Returns:
        Optional[OAuth2TokenCredentials]
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

    return OAuth2TokenCredentials(**oauth2_request.json())


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


def get_user_guilds(access_token: str) -> Tuple[bool, Optional[List[DiscordServer]]]:
    """
    Get user's guilds from Discord.
    Boolean in return defines whether response was success.

    Args:
        access_token: str
    Returns:
        Tuple[bool, Optional[List[DiscordServer]]]
    """
    get_guilds_request = requests.get(
        '{0}/users/@me/guilds'.format(
            os.getenv('DISCORD_ENDPOINT'),
        ),
        headers={
            'Authorization': 'Bearer {0}'.format(
                access_token,
            ),
        },
    )

    try:
        get_guilds_request.raise_for_status()
    except requests.HTTPError:
        return (False, None)

    raw_guilds = get_guilds_request.json()
    guilds = []

    for raw_guild in raw_guilds:
        permissions = raw_guild.get('permissions')
        icon_hash = raw_guild.get('icon')

        if permissions is None:
            continue

        if (
            DiscordPermission.administrator & int(permissions)
            != DiscordPermission.administrator
        ):
            continue

        raw_guild['permissions'] = int(permissions)
        raw_guild['icon'] = 'https://cdn.discordapp.com/icons/{0}/{1}.png'.format(
            raw_guild['id'],
            icon_hash,
        )

        guilds.append(DiscordServer(**raw_guild))

    return (True, guilds) if guilds else (True, None)


def refresh_oauth2_credentials(refresh_token: str) -> Optional[OAuth2TokenCredentials]:
    """
    Refresh oauth2 credentials.

    Args:
        refresh_token: str
    Returns:
        Optional[OAuth2TokenCredentials]
    """
    refresh_request = requests.post(
        '{0}/oauth2/token'.format(
            os.getenv('DISCORD_ENDPOINT'),
        ),
        data={
            'client_id': os.getenv('CLIENT_ID'),
            'client_secret': os.getenv('CLIENT_SECRET'),
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    )

    try:
        refresh_request.raise_for_status()
    except requests.HTTPError:
        return None

    return OAuth2TokenCredentials(**refresh_request.json())
