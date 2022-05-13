from __future__ import annotations

from dataclasses import dataclass

from app.models import InfractorSettingsModel


@dataclass
class TextedInfractorSettings:
    """Represents texted `infractor` settings"""

    infractor_is_enabled: str
    bad_words_is_enabled: str
    link_filter_is_enabled: str
    spam_detector_is_enabled: str

    @staticmethod
    def get_texted_settings(
        settings: InfractorSettingsModel,
    ) -> TextedInfractorSettings:
        """
        Build texted settings from model

        Params:
            settings: InfractorSettingsModel
        """
        data = {}

        if settings.infractor_is_enabled is True:
            data['infractor_is_enabled'] = '🟢'
        else:
            data['infractor_is_enabled'] = '⚫️'

        if settings.bad_words_is_enabled is True:
            data['bad_words_is_enabled'] = '☑️ Enabled'
        else:
            data['bad_words_is_enabled'] = '❌ Disabled'

        if settings.link_filter_is_enabled is True:
            data['link_filter_is_enabled'] = '☑️ Enabled'
        else:
            data['link_filter_is_enabled'] = '❌ Disabled'

        if settings.spam_detector_is_enabled is True:
            data['spam_detector_is_enabled'] = '☑️ Enabled'
        else:
            data['spam_detector_is_enabled'] = '❌ Disabled'

        return TextedInfractorSettings(**data)
