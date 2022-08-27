from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from api.routes.auth import discord
from api.routes.discord import get_guilds
from api.routes.status import healthcheck

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')
app.include_router(discord.router)
app.include_router(get_guilds.router)
app.include_router(healthcheck.router)


def custom_openapi():
    """Define OpenAPI overwrites for documentation."""
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


app.openapi = custom_openapi
