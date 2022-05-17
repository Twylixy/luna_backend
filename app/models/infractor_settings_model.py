import peewee

from app.models.base_model import BaseModel
from app.models.guild_model import GuildModel


class InfractorSettingsModel(BaseModel):
    """Represents `infractor's` settings model"""

    guild_id = peewee.ForeignKeyField(GuildModel, on_delete='CASCADE')
    infractor_is_enabled = peewee.BooleanField(default=False)
    bad_words_is_enabled = peewee.BooleanField(default=False)
    bad_words_dictionary = peewee.TextField(null=True)
    link_filter_is_enabled = peewee.BooleanField(default=False)
    link_filter_dictionary = peewee.TextField(null=True)
    spam_detector_is_enabled = peewee.BooleanField(default=False)

    class Meta:
        db_table = 'infractor_settings'
