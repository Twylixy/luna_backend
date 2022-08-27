from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session

from api.database.models import TokenModel, UserModel


def get_user_by_discord_id(session: Session, discord_id: int) -> Optional[UserModel]:
    """
    Return user object from database.

    Args:
      session: Session
      discord_id: int
    Returns:
      Optional[UserModel]
    """
    return session.query(UserModel).filter(UserModel.discord_id == discord_id).first()


def get_token_by_discord_id(session: Session, discord_id: int) -> Optional[TokenModel]:
    """
    Return token object from database.

    Args:
      session: Session
      discord_id: int
    Returns:
      Optional[TokenModel]
    """
    return session.query(TokenModel).filter(TokenModel.discord_id == discord_id).first()


def get_token_by_bearer(session: Session, bearer_token: str) -> Optional[TokenModel]:
    """
    Return token object from database.

    Args:
      session: Session
      discord_id: int
    Returns:
      Optional[TokenModel]
    """
    return (
        session.query(TokenModel).filter(TokenModel.bearer_token == bearer_token).first()
    )


def create_user(
    session: Session,
    discord_id: int,
    email: Optional[str] = None,
) -> UserModel:
    """
    Create and return user object from database.

    Args:
      session: Session
      discord_id: int
      email: Optional[str]
    Returns:
      UserModel
    """
    user = UserModel(discord_id=discord_id, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


def create_token(
    session: Session,
    discord_id: int,
    bearer_token: str,
    access_token: str,
    refresh_token: str,
    expires: Optional[int] = None,
) -> TokenModel:
    """
    Create and return token object from database.

    Args:
      session: Session
      discord_id: int
      bearer_token: str
      access_token: str
      refresh_token: str
      expires: Optional[int]
    Returns:
      TokenModel
    """
    token = TokenModel(
        discord_id=discord_id,
        bearer_token=bearer_token,
        access_token=access_token,
        refresh_token=refresh_token,
    )
    session.add(token)
    session.commit()
    session.refresh(token)

    return token


def update_user(
    session: Session,
    discord_id: int,
    email: Optional[str] = None,
) -> UserModel:
    """
    Update and return user object from database.

    Args:
      session: Session
      discord_id: int
      email: Optional[str]
    Returns:
      UserModel
    """
    user: UserModel = (
        session.query(UserModel).filter(UserModel.discord_id == discord_id).first()
    )
    user.email = email
    session.commit()
    session.refresh()

    return user


def update_token(
    session: Session,
    discord_id: int,
    bearer_token: str,
    access_token: str,
    refresh_token: str,
    expires: Optional[int] = None,
) -> TokenModel:
    """
    Update and return token object from database.

    Args:
      session: Session
      discord_id: int
      bearer_token: str
      access_token: str
      refresh_token: str
      expires: Optional[int]
    Returns:
      TokenModel
    """
    token: TokenModel = (
        session.query(TokenModel).filter(TokenModel.id == discord_id).first()
    )
    token.bearer_token = bearer_token
    token.access_token = access_token
    token.refresh_token = refresh_token
    token.expires = datetime.now() + timedelta(seconds=604800)

    session.commit()
    session.refresh(token)

    return token
