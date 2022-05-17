import peewee

from app.models.base_model import BaseModel
from app.models.user_model import UserModel


class SavedMessageModel(BaseModel):
    """Represents a saved message model"""

    text = peewee.TextField(null=False)
    discord_id = peewee.ForeignKeyField(UserModel, on_delete='CASCADE')
    hidden = peewee.BooleanField(default=False)

    class Meta:
        db_table = 'saved_messages'
