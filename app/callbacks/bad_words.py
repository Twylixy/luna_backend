import discord


async def change_bad_words_state_callback(interaction: discord.Interaction) -> None:
    """Callback for `edit_bad_words`"""
    await interaction.response.edit_message(embed=None, content='Got event', view=None)


async def edit_bad_words_callback(interaction: discord.Interaction) -> None:
    """Callback for `edit_bad_words`"""
    await interaction.response.edit_message(embed=None, content='Got event', view=None)
