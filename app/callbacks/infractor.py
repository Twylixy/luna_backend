import discord
from discord.ui import Button, View

from app.helpers import EMBED_DEFAULT_COLOR, TextedInfractorSettings
from app.models import InfractorSettingsModel

from .bad_words import (
    back_to_infractor_callback,
    change_bad_words_state_callback,
    edit_bad_words_callback,
)


async def bad_messages_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `bad_messages_menu` button id

    Params:
        interaction: discord.Interaction
    """
    infractor_settings = InfractorSettingsModel.get(
        guild_id=interaction.guild.id,
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
        change_bad_words_state_button_label = 'off'
        change_bad_words_state_button_style = discord.ButtonStyle.red
    else:
        change_bad_words_state_button_label = 'on'
        change_bad_words_state_button_style = discord.ButtonStyle.green

    change_bad_words_state_button = Button(
        label=f'Turn {change_bad_words_state_button_label}',
        style=change_bad_words_state_button_style,
    )
    edit_bad_words_button = Button(label='Edit words', style=discord.ButtonStyle.gray)
    back_to_infractor_button = Button(label='Back', style=discord.ButtonStyle.gray)

    change_bad_words_state_button.callback = change_bad_words_state_callback
    edit_bad_words_button.callback = edit_bad_words_callback
    back_to_infractor_button.callback = back_to_infractor_callback

    view = View(
        change_bad_words_state_button, edit_bad_words_button, back_to_infractor_button
    )

    await interaction.response.edit_message(embed=bad_messages_menu_embed, view=view)


async def link_filter_menu_callback(interaction: discord.Interaction) -> None:
    """Callback for `bad_messages_menu` button id

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(embed=None, content='Got event', view=None)


async def spam_detector_menu_callback(interaction: discord.Interaction) -> None:
    """Callback for `bad_messages_menu` button id

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(embed=None, content='Got event', view=None)
