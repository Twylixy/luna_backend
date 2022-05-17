from typing import Awaitable, Optional, Tuple, Union

import discord
from discord import Embed, Interaction
from discord.commands.context import ApplicationContext
from discord.ui import Button, View

from app.helpers.constants import EMBED_DEFAULT_COLOR
from app.helpers.settings_to_text import TextedInfractorSettings
from app.models.infractor_settings_model import InfractorSettingsModel


def get_spam_detector_view(
    ctx: Union[ApplicationContext, Interaction],
    change_spam_detector_state_callback: Awaitable[Interaction],
    configure_spam_detector_callback: Awaitable[Interaction],
    to_infractor_callback: Awaitable[Interaction],
    infractor_settings: Optional[InfractorSettingsModel] = None,
) -> Tuple[View, Embed]:
    """
    Create `spam_detector` view

    Params:
        ctx: Union[ApplicationContext, Interaction]
        change_spam_detector_state_callback: Awaitable[Interaction]
        configure_spam_detector_callback: Awaitable[Interaction]
        to_infractor_callback: Awaitable[Interaction]
        infractor_settings: InfractorSettingsModel
    """
    if infractor_settings is None:
        infractor_settings: InfractorSettingsModel = InfractorSettingsModel.get(
            guild_id=ctx.guild.id,
        )

    texted_infractor_settings = TextedInfractorSettings.get_texted_settings(
        infractor_settings,
    )

    spam_detector_embed = (
        discord.Embed(
            title='🌊 Spam Detector Module',
            description='Firewall for spammers in your text channels',
            color=EMBED_DEFAULT_COLOR,
        )
        .add_field(
            name='State',
            value=texted_infractor_settings.spam_detector_is_enabled,
            inline=True,
        )
        .add_field(
            name='Triggers Today',
            value='N/A',
            inline=True,
        )
        .set_footer(text='The best way to control spammers')
    )

    if infractor_settings.spam_detector_is_enabled is True:
        change_spam_detector_state_button_label = 'Turn off'
        change_spam_detector_state_button_style = discord.ButtonStyle.red
    else:
        change_spam_detector_state_button_label = 'Turn on'
        change_spam_detector_state_button_style = discord.ButtonStyle.green

    change_spam_detector_state_button = Button(
        label=change_spam_detector_state_button_label,
        style=change_spam_detector_state_button_style,
    )
    configure_spam_detector_button = Button(
        label='Configure', style=discord.ButtonStyle.gray
    )
    to_infractor_button = Button(label='Back', style=discord.ButtonStyle.gray)

    change_spam_detector_state_button.callback = change_spam_detector_state_callback
    configure_spam_detector_button.callback = configure_spam_detector_callback
    to_infractor_button.callback = to_infractor_callback

    view = View(
        change_spam_detector_state_button,
        configure_spam_detector_button,
        to_infractor_button,
    )

    return view, spam_detector_embed
