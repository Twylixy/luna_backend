from datetime import datetime

from django.db import models


class UserModel(models.Model):
    """Represents a user model"""

    id = models.AutoField(primary_key=True)
    discord_id = models.BigIntegerField(null=False, blank=False, unique=True)

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'users'

    def __str__(self) -> None:
        return f'User {self.id}'


class SavedMessageModel(models.Model):
    """Represents a saved message model"""

    text = models.TextField(null=False, blank=False)
    discord_id = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        db_column='discord_id',
        to_field='discord_id',
    )
    hidden = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        db_table = 'saved_messages'
        verbose_name_plural = 'saved_messages'

    def __str__(self) -> None:
        return f'Saved Message {self.id}'
