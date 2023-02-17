import os
from typing import Union

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from api.database.engine import get_session
from api.database.models import GuildModel, GuildSettingsModel
from api.entities.database import DatabaseGuild
from api.entities.http import HTTPResponseCode
from api.requests.database.guild import CreateDatabaseGuildRequest
from api.responses.database.guild import (
    CreateDatabaseGuildResponse,
    DeleteDatabaseGuildResponse,
    GetDatabaseGuildResponse,
    UpdateDatabaseGuildResponse,
)
from api.responses.error import ErrorResponse

database_guild_crud_router = APIRouter(
    responses={
        HTTPResponseCode.bad_request: {'model': ErrorResponse},
        HTTPResponseCode.unauthorized: {'model': ErrorResponse},
        HTTPResponseCode.forbidden: {'description': 'Wrong token or not provided'},
    },
)
bearer_dependency = HTTPBearer(scheme_name='Bearer')


@database_guild_crud_router.get(
    '/{guild_id}',
    response_model=GetDatabaseGuildResponse,
)
async def get_guild(
    guild_id: int,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[GetDatabaseGuildResponse, JSONResponse]:
    """
    Get guild from database.

    Args:
        guild_id: int
    Returns:
        Union[GetDatabaseGuildResponse, ErrorResponse]
    """
    if bearer.credentials != os.getenv('DATABASE_API_KEY'):
        return JSONResponse(
            status_code=HTTPResponseCode.forbidden,
            content=ErrorResponse(
                status='failure',
                message='forbidden',
            ).dict(),
        )

    if (guild := session.query(GuildModel).filter_by(guild_id=guild_id).first()) is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='guild not found',
            ).dict(),
        )

    return GetDatabaseGuildResponse(
        status='success',
        guild=DatabaseGuild(
            id=guild.id,
            guild_id=guild.guild_id,
            settings_id=guild.settings_id,
        ),
    )


@database_guild_crud_router.post(
    '/create',
    response_model=CreateDatabaseGuildResponse,
)
async def create_guild(
    request: CreateDatabaseGuildRequest,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[CreateDatabaseGuildResponse, JSONResponse]:
    """
    Create guild in database.

    Args:
        guild_id: int
    Returns:
        Union[CreateDatabaseGuildResponse, ErrorResponse]
    """
    if bearer.credentials != os.getenv('DATABASE_API_KEY'):
        return JSONResponse(
            status_code=HTTPResponseCode.forbidden,
            content=ErrorResponse(
                status='failure',
                message='forbidden',
            ).dict(),
        )

    if (
        guild := session.query(GuildModel).filter_by(guild_id=request.guild_id).first()
    ) is not None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='guild already exists',
            ).dict(),
        )

    guild = GuildModel(guild_id=request.guild_id)
    session.add(guild)
    session.commit()
    session.refresh(guild)

    settings = GuildSettingsModel(guild_id=request.guild_id)
    session.add(settings)
    session.commit()

    guild.settings_id = settings.id
    session.commit()

    return CreateDatabaseGuildResponse(
        status='success',
        guild=DatabaseGuild(
            id=guild.id,
            guild_id=guild.guild_id,
            settings_id=guild.settings_id,
        ),
    )


@database_guild_crud_router.patch(
    '/update/{guild_id}',
    response_model=UpdateDatabaseGuildResponse,
)
async def update_guild(
    guild_id: int,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[UpdateDatabaseGuildResponse, JSONResponse]:
    """
    Update guild in database.

    Args:
        guild_id: int
    Returns:
        Union[UpdateDatabaseGuildResponse, ErrorResponse]
    """
    if bearer.credentials != os.getenv('DATABASE_API_KEY'):
        return JSONResponse(
            status_code=HTTPResponseCode.forbidden,
            content=ErrorResponse(
                status='failure',
                message='forbidden',
            ).dict(),
        )

    if (guild := session.query(GuildModel).filter_by(guild_id=guild_id).first()) is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='guild not found',
            ).dict(),
        )

    # TODO: update guild
    # session.commit()

    return UpdateDatabaseGuildResponse(
        status='success',
        guild=DatabaseGuild(
            id=guild.id,
            guild_id=guild.guild_id,
            settings_id=guild.settings_id,
        ),
    )


@database_guild_crud_router.delete(
    '/delete/{guild_id}',
    response_model=DeleteDatabaseGuildResponse,
)
async def delete_guild(
    guild_id: int,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[DeleteDatabaseGuildResponse, JSONResponse]:
    """
    Delete guild from database.

    Args:
        guild_id: int
    Returns:
        Union[DeleteDatabaseGuildResponse, ErrorResponse]
    """
    if bearer.credentials != os.getenv('DATABASE_API_KEY'):
        return JSONResponse(
            status_code=HTTPResponseCode.forbidden,
            content=ErrorResponse(
                status='failure',
                message='forbidden',
            ).dict(),
        )

    if (guild := session.query(GuildModel).filter_by(guild_id=guild_id).first()) is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='guild not found',
            ).dict(),
        )

    session.delete(guild)
    session.commit()

    return DeleteDatabaseGuildResponse(status='success')
