from django.db import models


class GuildModel(models.Model):
    """Represents a guild model."""

    id = models.AutoField(primary_key=True)
    guild_id = models.BigIntegerField(null=False, blank=False, unique=True)

    class Meta:
        db_table = 'guilds'
        verbose_name_plural = 'guilds'

    def __str__(self):
        return f'Guild {self.guild_id}'
