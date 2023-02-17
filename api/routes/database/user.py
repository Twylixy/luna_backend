import os
from typing import Union

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from api.database.engine import get_session
from api.database.models import UserModel
from api.entities.database import DatabaseUser
from api.entities.http import HTTPResponseCode
from api.requests.database.user import (
    CreateDatabaseUserRequest,
    UpdateDatabaseUserRequest,
)
from api.responses.database.user import (
    CreateDatabaseUserResponse,
    DeleteDatabaseUserResponse,
    GetDatabaseUserResponse,
    UpdateDatabaseUserResponse,
)
from api.responses.error import ErrorResponse

database_user_crud_router = APIRouter(
    responses={
        HTTPResponseCode.bad_request: {'model': ErrorResponse},
        HTTPResponseCode.unauthorized: {'model': ErrorResponse},
        HTTPResponseCode.forbidden: {'description': 'Wrong token or not provided'},
    },
)
bearer_dependency = HTTPBearer(scheme_name='Bearer')


@database_user_crud_router.get(
    '/{discord_id}',
    response_model=GetDatabaseUserResponse,
)
async def get_user(
    discord_id: int,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[GetDatabaseUserResponse, JSONResponse]:
    """
    Get user from database.

    Args:
        discord_id: int
    Returns:
        Union[GetDatabaseUserResponse, ErrorResponse]
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
        user := session.query(UserModel).filter_by(discord_id=discord_id).first()
    ) is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='user not found',
            ).dict(),
        )

    return GetDatabaseUserResponse(
        status='success',
        user=DatabaseUser(
            id=user.id,
            discord_id=user.discord_id,
            email=user.email,
        ),
    )


@database_user_crud_router.post(
    '/create',
    response_model=CreateDatabaseUserResponse,
)
async def create_user(
    request: CreateDatabaseUserRequest,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[CreateDatabaseUserResponse, JSONResponse]:
    """
    Create user in database.

    Args:
        discord_id: int
        email: str
    Returns:
        Union[CreateDatabaseUserResponse, ErrorResponse]
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
        user := session.query(UserModel).filter_by(discord_id=request.discord_id).first()
    ) is not None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='user already exists',
            ).dict(),
        )

    user = UserModel(
        discord_id=request.discord_id,
        email=request.email,
    )
    session.add(user)
    session.commit()

    return CreateDatabaseUserResponse(
        status='success',
        user=DatabaseUser(
            id=user.id,
            discord_id=user.discord_id,
            email=user.email,
        ),
    )


@database_user_crud_router.patch(
    '/update/{discord_id}',
    response_model=UpdateDatabaseUserResponse,
)
async def update_user(
    discord_id: int,
    request: UpdateDatabaseUserRequest,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[UpdateDatabaseUserResponse, JSONResponse]:
    """
    Update user in database.

    Args:
        discord_id: int
        email: str
    Returns:
        Union[UpdateDatabaseUserResponse, ErrorResponse]
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
        user := session.query(UserModel).filter_by(discord_id=discord_id).first()
    ) is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='user not found',
            ).dict(),
        )

    user.email = request.email
    session.commit()

    return UpdateDatabaseUserResponse(
        status='success',
        user=DatabaseUser(
            id=user.id,
            discord_id=user.discord_id,
            email=user.email,
        ),
    )


@database_user_crud_router.delete(
    '/delete/{discord_id}',
    response_model=DeleteDatabaseUserResponse,
)
async def delete_user(
    discord_id: int,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_dependency),
    session: Session = Depends(get_session),
) -> Union[DeleteDatabaseUserResponse, JSONResponse]:
    """
    Delete user from database.

    Args:
        user_id: int
    Returns:
        Union[DeleteDatabaseUserResponse, ErrorResponse]
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
        user := session.query(UserModel).filter_by(discord_id=discord_id).first()
    ) is None:
        return JSONResponse(
            status_code=HTTPResponseCode.bad_request,
            content=ErrorResponse(
                status='failure',
                message='user not found',
            ).dict(),
        )

    session.delete(user)
    session.commit()

    return DeleteDatabaseUserResponse(status='success')
