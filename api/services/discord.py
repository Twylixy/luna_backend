import logging
import os
from typing import List, Optional

import aiohttp

from api.entities.discord import (
    DiscordGuild,
    DiscordUser,
    OAuth2TokenCredentials,
)

# define admin rights from Discord
admin_perms = 0x80

logger = logging.getLogger('services.discord')


async def get_oauth2_credentials(
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
    oauth2_request = None
    url = '{0}/oauth2/token'.format(os.getenv('DISCORD_ENDPOINT'))
    payload = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'grant_type': 'authorization_code',
        'code': discord_code,
        'redirect_uri': redirect_uri,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=payload) as response:
            try:
                response.raise_for_status()
            except aiohttp.ClientResponseError as error:
                logger.error(error.message)
                return None
            oauth2_request = await response.json()

    return OAuth2TokenCredentials(**oauth2_request)


async def get_discord_user(access_token: str) -> Optional[DiscordUser]:
    """
    Get user from discord.

    Args:
        access_token: str
    Returns:
        Optional[DiscordUser]
    """
    get_user_request = None
    url = '{0}/users/@me'.format(os.getenv('DISCORD_ENDPOINT'))
    headers = {'Authorization': 'Bearer {0}'.format(access_token)}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            try:
                response.raise_for_status()
            except aiohttp.ClientResponseError as error:
                logger.error(error.message)
                return None
            get_user_request = await response.json()

    avatar = get_user_request.get('avatar')

    if avatar is not None:
        new_avatar = 'https://cdn.discordapp.com/avatars/{0}/{1}.png'.format(
            get_user_request['id'],
            avatar,
        )
        get_user_request['avatar'] = new_avatar

    return DiscordUser(**get_user_request)


async def get_user_guilds(access_token: str) -> Optional[List[DiscordGuild]]:
    """
    Get user's guilds from Discord.

    Args:
        access_token: str
    Returns:
        Optional[List[DiscordGuild]]
    """
    get_guilds_request = None
    url = '{0}/users/@me/guilds'.format(os.getenv('DISCORD_ENDPOINT'))
    headers = {'Authorization': 'Bearer {0}'.format(access_token)}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            try:
                response.raise_for_status()
            except aiohttp.ClientResponseError as error:
                logger.error(error.message)
                return None
            get_guilds_request = await response.json()

    guilds = []

    for raw_guild in get_guilds_request:
        permissions = raw_guild.get('permissions')
        icon_hash = raw_guild.get('icon')

        if permissions is None:
            continue

        if admin_perms & int(permissions) != admin_perms:
            continue

        raw_guild['permissions'] = int(permissions)
        raw_guild['icon'] = 'https://cdn.discordapp.com/icons/{0}/{1}.png'.format(
            raw_guild['id'],
            icon_hash,
        )

        guilds.append(DiscordGuild(**raw_guild))

    return guilds


async def refresh_oauth2_credentials(
    refresh_token: str,
) -> Optional[OAuth2TokenCredentials]:
    """
    Refresh oauth2 credentials.

    Args:
        refresh_token: str
    Returns:
        Optional[OAuth2TokenCredentials]
    """
    refresh_request = None
    url = '{0}/oauth2/token'.format(os.getenv('DISCORD_ENDPOINT'))
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=payload) as response:
            try:
                response.raise_for_status()
            except aiohttp.ClientResponseError as error:
                logger.error(error.message)
                return None
            refresh_request = await response.json()

    return OAuth2TokenCredentials(**refresh_request)
