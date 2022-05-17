from typing import Awaitable, Optional, Tuple, Union

import discord
from discord import Embed, Interaction
from discord.commands import ApplicationContext
from discord.ui import Button, View

from app.helpers.constants import EMBED_DEFAULT_COLOR
from app.helpers.settings_to_text import TextedInfractorSettings
from app.models.infractor_settings_model import InfractorSettingsModel


def get_bad_words_view(
    ctx: Union[ApplicationContext, Interaction],
    change_bad_words_state_callback: Awaitable[Interaction],
    configure_bad_words_callback: Awaitable[Interaction],
    to_infractor_callback: Awaitable[Interaction],
    infractor_settings: Optional[InfractorSettingsModel] = None,
) -> Tuple[View, Embed]:
    """
    Create `bad messages` view

    Params:
        interaction: Union[ApplicationContext, Interaction]
        change_bad_words_state_callback: Awaitable[Interaction]
        configure_bad_words_callback: Awaitable[Interaction]
        to_infractor_callback: Awaitable[Interaction]
        infractor_settings: Optional[InfractorSettingsModel]
    """

    if infractor_settings is None:
        infractor_settings = InfractorSettingsModel.get(
            guild_id=ctx.guild.id,
        )

    texted_infractor_settings = TextedInfractorSettings.get_texted_settings(
        infractor_settings,
    )

    bad_messages_menu_embed = (
        discord.Embed(
            title='💬 Bad Messages Module',
            description="Help's you to block bad words on your server",
            color=EMBED_DEFAULT_COLOR,
        )
        .add_field(
            name='State',
            value=texted_infractor_settings.bad_words_is_enabled,
            inline=True,
        )
        .add_field(
            name='Triggers Today',
            value='N/A',
            inline=True,
        )
        .set_footer(text="Stay calm while I'm watching")
    )

    if infractor_settings.bad_words_is_enabled is True:
        change_bad_words_state_button_label = 'Turn off'
        change_bad_words_state_button_style = discord.ButtonStyle.red
    else:
        change_bad_words_state_button_label = 'Turn on'
        change_bad_words_state_button_style = discord.ButtonStyle.green

    change_bad_words_state_button = Button(
        label=change_bad_words_state_button_label,
        style=change_bad_words_state_button_style,
    )
    configure_bad_words_button = Button(
        label='Configure', style=discord.ButtonStyle.gray
    )
    to_infractor_button = Button(label='Back', style=discord.ButtonStyle.gray)

    change_bad_words_state_button.callback = change_bad_words_state_callback
    configure_bad_words_button.callback = configure_bad_words_callback
    to_infractor_button.callback = to_infractor_callback

    view = View(
        change_bad_words_state_button,
        configure_bad_words_button,
        to_infractor_button,
    )

    return view, bad_messages_menu_embed
