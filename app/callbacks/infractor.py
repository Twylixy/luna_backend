import discord
from discord.ui import Button, View

from app.helpers import EMBED_DEFAULT_COLOR

from .bad_words import change_bad_words_state_callback, edit_bad_words_callback


async def bad_messages_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `bad_messages_menu` button id

    Params:
        interaction: discord.Interaction
    """
    bad_messages_menu_embed = (
        discord.Embed(
            title='Bad Messages Module',
            description="Help's you to block bad words on your server",
            color=EMBED_DEFAULT_COLOR,
        )
        .add_field(
            name='State',
            value='☑️ Enabled',
            inline=True,
        )
        .add_field(
            name='Triggers Today',
            value='35',
            inline=True,
        )
        .set_footer(text="Stay calm when I'm wathing")
    )

    change_bad_words_state_button = Button(
        label='Turn off',
        style=discord.ButtonStyle.gray,
    )
    edit_bad_words_button = Button(label='Edit words', style=discord.ButtonStyle.gray)

    change_bad_words_state_button.callback = change_bad_words_state_callback
    edit_bad_words_button.callback = edit_bad_words_callback

    view = View(
        change_bad_words_state_button,
        edit_bad_words_button,
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
