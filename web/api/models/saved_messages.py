from api.models.guild import GuildModel
from api.models.user import UserModel
from django.db import models


class SavedMessagesModel(models.Model):
    """Represents a saved messages model."""

    id = models.AutoField(primary_key=True)
    text = models.TextField(null=False, blank=False)
    discord_id = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        db_column='discord_id',
        to_field='discord_id',
    )
    guild_id = models.ForeignKey(
        GuildModel,
        on_delete=models.CASCADE,
        db_column='guild_id',
        to_field='guild_id',
    )
    hidden = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        db_table = 'saved_messages'
        verbose_name_plural = 'saved_messages'

    def __str__(self) -> None:
        return f'Saved Message {self.id}'
