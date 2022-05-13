import discord
from app.helpers.views import get_bad_words_view
from app.callbacks import (
    change_bad_words_state_callback,
    edit_bad_words_callback,
    back_to_infractor_callback,
)


async def bad_messages_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `bad_messages_menu` button id

    Params:
        interaction: discord.Interaction
    """
    view, bad_messages_menu_embed = get_bad_words_view(
        interaction,
        change_bad_words_state_callback,
        edit_bad_words_callback,
        back_to_infractor_callback,
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
