import discord

from app.helpers.views import get_bad_words_view
from app.models import InfractorSettingsModel


async def change_bad_words_state_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `edit_bad_words` button

    Params:
        interaction: discord.Interaction
    """

    infractor_settings: InfractorSettingsModel = InfractorSettingsModel.get(
        guild_id=interaction.guild.id,
    )

    if infractor_settings.bad_words_is_enabled is True:
        infractor_settings.bad_words_is_enabled = False
    else:
        infractor_settings.bad_words_is_enabled = True

    infractor_settings.save()

    view, bad_words_menu_embed = get_bad_words_view(
        interaction,
        change_bad_words_state_callback,
        edit_bad_words_callback,
        back_to_infractor_callback,
        infractor_settings=infractor_settings,
    )
    await interaction.response.edit_message(embed=bad_words_menu_embed, view=view)


async def edit_bad_words_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `edit_bad_words` button

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(embed=None, content='Got event', view=None)


async def back_to_infractor_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `back_to_infractor` button

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(embed=None, content='Got event', view=None)
