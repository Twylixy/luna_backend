import discord

from app.models.infractor_settings_model import InfractorSettingsModel
from app.views.bad_words_view import get_bad_words_view
from app.views.infractor_view import get_infractor_view
from app.views.link_filter_view import get_link_filter_view
from app.views.spam_detector_view import get_spam_detector_view


async def bad_messages_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `bad_messages_menu` button

    Params:
        interaction: discord.Interaction
    """
    view, bad_messages_menu_embed = get_bad_words_view(
        interaction,
        change_bad_words_state_callback,
        configure_bad_words_callback,
        to_infractor_callback,
    )
    await interaction.response.edit_message(embed=bad_messages_menu_embed, view=view)


async def change_bad_words_state_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `change_bad_words_state` button

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
        configure_bad_words_callback,
        to_infractor_callback,
        infractor_settings=infractor_settings,
    )
    await interaction.response.edit_message(
        embed=bad_words_menu_embed,
        content=text_to_content,
        view=view,
    )


async def configure_bad_words_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `configure_bad_words` button

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(
        content='For `Bad Words` configuration use **[online-panel](https://luna.staypony.space/)**'
    )


async def link_filter_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `link_filter_menu` button

    Params:
        interaction: discord.Interaction
    """
    view, link_filter_menu_embed = get_link_filter_view(
        interaction,
        change_link_filter_state_callback,
        configure_link_filter_callback,
        to_infractor_callback,
    )
    await interaction.response.edit_message(
        embed=link_filter_menu_embed, content='', view=view
    )


async def change_link_filter_state_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `change_link_filter_state` button

    Params:
        interaction: discord.Interaction
    """
    infractor_settings: InfractorSettingsModel = InfractorSettingsModel.get(
        guild_id=interaction.guild.id,
    )

    if infractor_settings.link_filter_is_enabled is True:
        infractor_settings.link_filter_is_enabled = False
        text_to_content = 'The `Link Filter` module has been **disabled**'
    else:
        infractor_settings.link_filter_is_enabled = True
        text_to_content = 'The `Link Filter` module has been **enabled**'

    infractor_settings.save()

    view, link_filter_menu_embed = get_link_filter_view(
        interaction,
        change_link_filter_state_callback,
        configure_link_filter_callback,
        to_infractor_callback,
        infractor_settings=infractor_settings,
    )
    await interaction.response.edit_message(
        embed=link_filter_menu_embed,
        content=text_to_content,
        view=view,
    )


async def configure_link_filter_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `configure_link_filter` button

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(
        content='For `Link Filter` configuration use **[online-panel](https://luna.staypony.space/)**'
    )


async def spam_detector_menu_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `spam_detector_menu` button

    Params:
        interaction: discord.Interaction
    """
    view, spam_detector_embed = get_spam_detector_view(
        interaction,
        change_spam_detector_state_callback,
        configure_spam_detector_callback,
        to_infractor_callback,
    )
    await interaction.response.edit_message(
        embed=spam_detector_embed, content='', view=view
    )


async def change_spam_detector_state_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `change_spam_detector` button

    Params:
        interaction: discord.Interaction
    """
    infractor_settings: InfractorSettingsModel = InfractorSettingsModel.get(
        guild_id=interaction.guild.id,
    )

    if infractor_settings.spam_detector_is_enabled is True:
        infractor_settings.spam_detector_is_enabled = False
        text_to_content = 'The `Spam Detector` module has been **disabled**'
    else:
        infractor_settings.spam_detector_is_enabled = True
        text_to_content = 'The `Spam Detector` module has been **enabled**'

    infractor_settings.save()

    view, spam_detector_embed = get_spam_detector_view(
        interaction,
        change_spam_detector_state_callback,
        configure_spam_detector_callback,
        to_infractor_callback,
        infractor_settings=infractor_settings,
    )
    await interaction.response.edit_message(
        embed=spam_detector_embed,
        content=text_to_content,
        view=view,
    )


async def configure_spam_detector_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `configure_spam_detector` button

    Params:
        interaction: discord.Interaction
    """
    await interaction.response.edit_message(
        content='For `Spam Detector` configuration use **[online-panel](https://luna.staypony.space/)**'
    )


async def change_infractor_state_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `change_infractor_state` button

    Params:
        interaction: discord.Interaction
    """
    infractor_settings: InfractorSettingsModel = InfractorSettingsModel.get(
        guild_id=interaction.guild.id,
    )

    if infractor_settings.infractor_is_enabled is True:
        infractor_settings.infractor_is_enabled = False
        text_to_content = 'The `Infractor` module has been **disabled**'
    else:
        infractor_settings.infractor_is_enabled = True
        text_to_content = 'The `Infractor` module has been **enabled**'

    infractor_settings.save()

    view, infractor_embed = get_infractor_view(
        interaction,
        change_infractor_state_callback,
        bad_messages_menu_callback,
        link_filter_menu_callback,
        spam_detector_menu_callback,
        infractor_settings=infractor_settings,
    )
    await interaction.response.edit_message(
        embed=infractor_embed,
        content=text_to_content,
        view=view,
    )


async def to_infractor_callback(interaction: discord.Interaction) -> None:
    """
    Callback for `to_infractor_menu` button

    Params:
        interaction: discord.Interaction
    """
    view, infractor_menu_embed = get_infractor_view(
        interaction,
        change_infractor_state_callback,
        bad_messages_menu_callback,
        link_filter_menu_callback,
        spam_detector_menu_callback,
    )
    await interaction.response.edit_message(
        content='',
        view=view,
        embed=infractor_menu_embed,
    )
