from django.db import models


class UserModel(models.Model):
    """Represents a user model."""

    id = models.AutoField(primary_key=True)
    discord_id = models.BigIntegerField(null=False, blank=False, unique=True)
    email = models.TextField(null=True, blank=True, default=None)

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'users'

    def __str__(self) -> None:
        return f'User {self.id}'
