from api.models.user import UserModel
from django.db import models


class TokensModel(models.Model):
    """Represents tokens model."""

    id = models.AutoField(primary_key=True)
    discord_id = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        db_column='discord_id',
        to_field='discord_id',
    )
    token = models.TextField(null=True, blank=False)
    discord_token = models.TextField(null=True, blank=False)
    discord_refresh_token = models.TextField(null=True, blank=False)
    epires = models.DateTimeField(null=True, blank=False)

    class Meta:
        db_table = 'tokens'
        verbose_name_plural = 'tokens'

    def __str__(self) -> None:
        return f'Token {self.id} of user {self.discord_id}'
