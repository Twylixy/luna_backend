from django.db import models


class GuildModel(models.Model):
    """Represents a guild model"""

    guild_id = models.BigIntegerField(null=False, blank=False, unique=True)

    class Meta:
        db_table = 'guilds'
        verbose_name_plural = 'guilds'

    def __str__(self):
        return f'Guild {self.guild_id}'


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


class InfractorSettingsModel(models.Model):
    """Represents infractor's bad words settings model"""

    guild_id = models.ForeignKey(
        GuildModel,
        on_delete=models.CASCADE,
        db_column='guild_id',
        to_field='guild_id',
    )
    infractor_is_enabled = models.BooleanField(default=False, null=True, blank=True)
    bad_words_is_enabled = models.BooleanField(default=False, null=True, blank=True)
    bad_words_dictionary = models.TextField(null=True, blank=True)
    link_filter_is_enabled = models.BooleanField(default=False, null=True, blank=True)
    link_filter_dictionary = models.TextField(null=True, blank=True)
    spam_detector_is_enabled = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        db_table = 'infractor_settings'
        verbose_name_plural = 'infractor_settings'

    def __str__(self) -> str:
        return f'Infractor Settings {self.id}'
