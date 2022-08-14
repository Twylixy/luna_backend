from api.models.guild import GuildModel
from django.db import models


class InfractorSettingsModel(models.Model):
    """Represents infractor's bad words settings model."""

    id = models.AutoField(primary_key=True)
    guild_id = models.ForeignKey(
        GuildModel,
        on_delete=models.CASCADE,
        db_column='guild_id',
        to_field='guild_id',
    )
    infractor_is_enabled = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
    bad_words_is_enabled = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
    bad_words_dictionary = models.TextField(null=True, blank=True)
    link_filter_is_enabled = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
    link_filter_dictionary = models.TextField(null=True, blank=True)
    spam_detector_is_enabled = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'infractor_settings'
        verbose_name_plural = 'infractor_settings'

    def __str__(self) -> str:
        return f'Infractor Settings {self.id}'
