import discord

from app.modals import EditBadWordsModal
from app.models import InfractorSettingsModel
from app.views import get_bad_words_view, get_infractor_view


async def bad_messages_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `bad_messages_menu` button

    Params:
        interaction: discord.Interaction
    """
    view, bad_messages_menu_embed = get_bad_words_view(
        interaction,
        change_bad_words_state_callback,
        edit_bad_words_callback,
        to_infractor_callback,
    )
    await interaction.response.edit_message(embed=bad_messages_menu_embed, view=view)


async def link_filter_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `link_filter_menu` button

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(embed=None, content='Got event', view=None)


async def spam_detector_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `spam_detector_menu` button

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(embed=None, content='Got event', view=None)


async def to_infractor_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `to_infractor_menu` button

    Params:
        interaction: discord.Interaction
    """
    view, infractor_menu_embed = get_infractor_view(
        interaction,
        bad_messages_menu_callback,
        link_filter_menu_callback,
        spam_detector_menu_callback,
    )
    await interaction.response.edit_message(
        content='',
        view=view,
        embed=infractor_menu_embed,
    )


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
        text_to_content = 'The `Bad Words` module has been **disabled**'
    else:
        infractor_settings.bad_words_is_enabled = True
        text_to_content = 'The `Bad Words` module has been **enabled**'

    infractor_settings.save()

    view, bad_words_menu_embed = get_bad_words_view(
        interaction,
        change_bad_words_state_callback,
        edit_bad_words_callback,
        to_infractor_callback,
        infractor_settings=infractor_settings,
    )
    await interaction.response.edit_message(
        embed=bad_words_menu_embed,
        content=text_to_content,
        view=view,
    )


async def edit_bad_words_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `edit_bad_words` button

    Params:
        interaction: discord.Interaction
    """
    infractor_settings = InfractorSettingsModel.get(guild_id=interaction.guild.id)
    modal = EditBadWordsModal(infractor_settings)

    await interaction.response.send_modal(modal=modal)
