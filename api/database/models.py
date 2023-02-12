from datetime import datetime, timedelta

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Text,
)

from api.database.engine import BaseModel


class GuildModel(BaseModel):
    """Represents a guild model."""

    __tablename__ = 'guilds'

    id = Column(Integer, primary_key=True)
    guild_id = Column(Integer, unique=True, nullable=False)
    settings_id = Column(
        Integer,
        ForeignKey('guild_settings.id', ondelete='CASCADE'),
        unique=True,
    )


class UserModel(BaseModel):
    """Represents a user model."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    discord_id = Column(BigInteger, unique=True, nullable=False)
    email = Column(Text, default=None)


class GuildSettingsModel(BaseModel):
    """Represents a guild_settings model."""

    __tablename__ = 'guild_settings'

    id = Column(Integer, primary_key=True)
    guild_id = Column(BigInteger, nullable=False)
    prefix = Column(Text, default='-', nullable=False)
    welcome_channel = Column(BigInteger, default=None)
    welcome_message = Column(Text, default=None)
    leave_channel = Column(BigInteger, default=None)
    leave_message = Column(Text, default=None)


class SavedMessageModel(BaseModel):
    """Represents a saved_messages model."""

    __tablename__ = 'saved_messages'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    discord_id = Column(BigInteger, ForeignKey('users.discord_id', ondelete='CASCADE'))
    guild_id = Column(BigInteger, ForeignKey('guilds.guild_id', ondelete='CASCADE'))
    hidden = Column(Boolean, default=False)


class TokenModel(BaseModel):
    """Represents a token model."""

    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True)
    discord_id = Column(BigInteger, ForeignKey('users.discord_id', ondelete='CASCADE'))
    bearer_token = Column(Text, nullable=False)
    access_token = Column(Text, nullable=False)
    refresh_token = Column(Text, nullable=False)
    expires = Column(DateTime, default=datetime.now() + timedelta(seconds=604800))
