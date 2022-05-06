import discord


async def bad_messages_menu_callback(interaction: discord.Interaction) -> None:
    """Callback for `bad_messages_menu` button id"""
    await interaction.response.edit_message(embed=None, content='Got event', view=None)


async def link_filter_menu_callback(interaction: discord.Interaction) -> None:
    """Callback for `bad_messages_menu` button id"""
    await interaction.response.edit_message(embed=None, content='Got event', view=None)


async def spam_detector_menu_callback(interaction: discord.Interaction) -> None:
    """Callback for `bad_messages_menu` button id"""
    await interaction.response.edit_message(embed=None, content='Got event', view=None)
