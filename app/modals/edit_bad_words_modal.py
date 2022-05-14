from discord import InputTextStyle, Interaction
from discord.ui import InputText, Modal

from app.models import InfractorSettingsModel


class EditBadWordsModal(Modal):
    """Represents a edit bad words modal"""

    def __init__(self, infractor_settings: InfractorSettingsModel) -> None:
        """
        Initialize a new edit bad words modal

        Params:
            luna_instance: discord.ext.commands.Bot
        """
        super().__init__(title='Edit Bad Words Dictionary')
        self.add_item(
            InputText(
                label='Bad words dictionary',
                placeholder='Enter here words, that must be detected (divide them by ",")',
                style=InputTextStyle.long,
                required=False,
                value=infractor_settings.bad_words_dictionary,
            )
        )

    async def callback(self, interaction: Interaction) -> None:
        """
        Callback for modal

        Params:
            interaction: discord.Interaction
        """
        infractor_settings: InfractorSettingsModel = InfractorSettingsModel.get(
            guild_id=interaction.guild.id,
        )
        infractor_settings.bad_words_dictionary = self.children[0].value
        infractor_settings.save()

        await interaction.response.edit_message(
            content='The `bad words` dictionary has been updated'
        )
