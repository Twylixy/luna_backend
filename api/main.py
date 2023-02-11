import logging
import os
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from api.routes.auth import discord
from api.routes.discord import get_guild, get_guilds, get_me
from api.routes.status import healthcheck

logging.basicConfig(
    format='%(levelname)s - %(name)s:\t%(message)s',  # noqa: WPS323
    level=int(os.getenv('LOGGING_LEVEL', logging.INFO)),
)

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')
app.include_router(discord.router)
app.include_router(get_guilds.router)
app.include_router(get_guild.router)
app.include_router(get_me.router)
app.include_router(healthcheck.router)


def custom_openapi() -> Dict[str, Any]:
    """
    Define OpenAPI overwrites for documentation.

    Returns:
        Dict[str, Any]: OpenAPI schema.
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title='Luna API',
        version='v1',
        description='The API service for Luna Discord Bot',
        routes=app.routes,
        contact={
            'name': 'The Staypony',
            'url': 'https://staypony.space/',
            'email': 'admin@staypony.space',
        },
        license_info={
            'name': 'BSD License',
        },
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# this line ignored because of bug in mypy
app.openapi = custom_openapi  # type: ignore[assignment]
