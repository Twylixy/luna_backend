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
    guild_id = Column(Integer, unique=True)


class UserModel(BaseModel):
    """Represents a user model."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    discord_id = Column(BigInteger, unique=True)
    email = Column(Text, default=None)


class InfractorSettingsModel(BaseModel):
    """Represents an infractor settings model."""

    __tablename__ = 'infractor_settings'

    id = Column(Integer, primary_key=True)
    guild_id = Column(BigInteger, ForeignKey('guilds.guild_id', ondelete='CASCADE'))
    infractor_is_enabled = Column(Boolean, default=False)
    bad_words_is_enabled = Column(Boolean, default=False)
    bad_words_dictionary = Column(Text, default=None)
    link_filter_is_enabled = Column(Boolean, default=False)
    link_filter_dictionary = Column(Text, default=None)
    spam_detector_is_enabled = Column(Boolean, default=False)


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
