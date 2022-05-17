from typing import Awaitable, Optional, Tuple, Union

import discord
from discord import Embed, Interaction
from discord.commands import ApplicationContext
from discord.ui import Button, View

from app.helpers.constants import EMBED_DEFAULT_COLOR
from app.helpers.settings_to_text import TextedInfractorSettings
from app.models.infractor_settings_model import InfractorSettingsModel


def get_infractor_view(
    ctx: Union[ApplicationContext, Interaction],
    change_infractor_state_callback: Awaitable[Interaction],
    bad_messages_menu_callback: Awaitable[Interaction],
    link_filter_menu_callback: Awaitable[Interaction],
    spam_detector_menu_callback: Awaitable[Interaction],
    infractor_settings: Optional[InfractorSettingsModel] = None,
) -> Tuple[View, Embed]:
    """
    Create `infractor` view

    Params:
        ctx: Union[ApplicationContext, Interaction]
        change_infractor_state_callback: Awaitable[Interaction]
        bad_messages_menu_callback: Awaitable[Interaction]
        link_filter_menu_callback: Awaitable[Interaction]
        spam_detector_menu_callback: Awaitable[Interaction]
        infractor_settings: InfractorSettingsModel
    """
    if infractor_settings is None:
        infractor_settings: InfractorSettingsModel = InfractorSettingsModel.get(
            guild_id=ctx.guild.id,
        )

    texted_infractor_settings = TextedInfractorSettings.get_texted_settings(
        infractor_settings,
    )

    infractor_embed = (
        discord.Embed(
            title=f'{texted_infractor_settings.infractor_is_enabled} Infractor | Dashboard',
            description='They cannot confronts to empress',
            color=EMBED_DEFAULT_COLOR,
        )
        .add_field(
            name='💬 Bad Messages',
            value=texted_infractor_settings.bad_words_is_enabled,
            inline=True,
        )
        .add_field(
            name='🌐 Link Filter',
            value=texted_infractor_settings.link_filter_is_enabled,
            inline=True,
        )
        .add_field(
            name='🌊 Spam Detector',
            value=texted_infractor_settings.spam_detector_is_enabled,
            inline=True,
        )
        .set_footer(text='The best way to control content')
    )

    if infractor_settings.infractor_is_enabled is True:
        change_infractor_state_button_label = 'Turn off'
        change_infractor_state_button_style = discord.ButtonStyle.red
    else:
        change_infractor_state_button_label = 'Turn on'
        change_infractor_state_button_style = discord.ButtonStyle.green

    change_infractor_state_button = Button(
        label=change_infractor_state_button_label,
        style=change_infractor_state_button_style,
    )
    bad_messages_button = Button(
        label='Bad Messages',
        style=discord.ButtonStyle.gray,
        emoji='💬',
    )
    link_filter_button = Button(
        label='Link Filter',
        style=discord.ButtonStyle.gray,
        emoji='🌐',
    )
    spam_detector_button = Button(
        label='Spam Detector',
        style=discord.ButtonStyle.gray,
        emoji='🌊',
    )

    change_infractor_state_button.callback = change_infractor_state_callback
    bad_messages_button.callback = bad_messages_menu_callback
    link_filter_button.callback = link_filter_menu_callback
    spam_detector_button.callback = spam_detector_menu_callback

    view = View(
        change_infractor_state_button,
        bad_messages_button,
        link_filter_button,
        spam_detector_button,
    )

    return view, infractor_embed
