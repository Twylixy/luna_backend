import logging
import os
from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from api.responses.error import ErrorResponse
from api.routes.database.guild import database_guild_crud_router
from api.routes.database.user import database_user_crud_router
from api.routes.discord.user.guild import user_guild_router
from api.routes.discord.user.me import user_me_router
from api.routes.oauth2.discord import discord_auth_router
from api.routes.status.healthcheck import healthcheck_router

logging.basicConfig(
    format='%(levelname)s - %(name)s:\t%(message)s',
    level=int(os.getenv('LOGGING_LEVEL', logging.INFO)),
)

app = FastAPI(
    docs_url='/api/docs',
    redoc_url='/api/redoc',
    openapi_url='/api/openapi.json',
)

app.include_router(
    database_guild_crud_router,
    prefix='/api/database/guilds',
    tags=['database'],
)
app.include_router(
    database_user_crud_router,
    prefix='/api/database/users',
    tags=['database'],
)
app.include_router(
    user_guild_router,
    prefix='/api/discord/users/guilds',
    tags=['discord'],
)
app.include_router(
    user_me_router,
    prefix='/api/discord/users/me',
    tags=['discord'],
)
app.include_router(
    discord_auth_router,
    prefix='/api/oauth2/discord',
    tags=['oauth2'],
)
app.include_router(
    healthcheck_router,
    prefix='/api/status',
    tags=['status'],
)


@app.exception_handler(500)
async def internal_server_error_handler(
    request: Request, exception: Exception
) -> JSONResponse:
    """
    Handle 500 errors.

    Args:
        request: Request
        exception: Exception
    Returns:
        ErrorResponse
    """
    logging.log(logging.ERROR, "500 Internal Server Error: (%s)", exception)
    logging.log(
        logging.ERROR,
        "Url: {0}\nPath params: {1}\nQuery params: {2}\nHeaders: {3}\nBody: {4}".format(
            request.url,
            request.path_params,
            request.query_params,
            request.headers,
            request.body,
        ),
    )

    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            status='failure',
            message='Internal Server Error (500)',
        ).dict(),
    )


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
            'url': os.getenv('SWAGGER_URL', 'https://staypony.space'),
            'email': os.getenv('SWAGGER_EMAIL', 'admin@staypony.space'),
        },
        license_info={
            'name': 'BSD License',
        },
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# this line ignored because of bug in mypy
app.openapi = custom_openapi  # type: ignore[assignment]
