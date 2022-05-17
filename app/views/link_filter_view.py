from typing import Awaitable, Optional, Tuple, Union

import discord
from discord import Embed, Interaction
from discord.commands.context import ApplicationContext
from discord.ui import Button, View

from app.helpers.constants import EMBED_DEFAULT_COLOR
from app.helpers.settings_to_text import TextedInfractorSettings
from app.models.infractor_settings_model import InfractorSettingsModel


def get_link_filter_view(
    ctx: Union[ApplicationContext, Interaction],
    change_link_filter_state_callback: Awaitable[Interaction],
    configure_link_filter_callback: Awaitable[Interaction],
    to_infractor_callback: Awaitable[Interaction],
    infractor_settings: Optional[InfractorSettingsModel] = None,
) -> Tuple[View, Embed]:
    """
    Create `link_filter` view

    Params:
        ctx: Union[ApplicationContext, Interaction]
        change_link_filter_state_callback: Awaitable[Interaction]
        configure_link_filter_callback: Awaitable[Interaction]
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

    link_filter_embed = (
        discord.Embed(
            title='🌐 Link Filter Module',
            description='Prevent send links in your text channels',
            color=EMBED_DEFAULT_COLOR,
        )
        .add_field(
            name='State',
            value=texted_infractor_settings.link_filter_is_enabled,
            inline=True,
        )
        .add_field(
            name='Triggers Today',
            value='N/A',
            inline=True,
        )
        .set_footer(text='The best way to control links')
    )

    if infractor_settings.link_filter_is_enabled is True:
        change_link_filter_state_button_label = 'Turn off'
        change_link_filter_state_button_style = discord.ButtonStyle.red
    else:
        change_link_filter_state_button_label = 'Turn on'
        change_link_filter_state_button_style = discord.ButtonStyle.green

    change_link_filter_state_button = Button(
        label=change_link_filter_state_button_label,
        style=change_link_filter_state_button_style,
    )
    configure_link_filter_button = Button(
        label='Configure', style=discord.ButtonStyle.gray
    )
    to_infractor_button = Button(label='Back', style=discord.ButtonStyle.gray)

    change_link_filter_state_button.callback = change_link_filter_state_callback
    configure_link_filter_button.callback = configure_link_filter_callback
    to_infractor_button.callback = to_infractor_callback

    view = View(
        change_link_filter_state_button,
        configure_link_filter_button,
        to_infractor_button,
    )

    return view, link_filter_embed
