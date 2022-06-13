from os import environ

import discord


class MessageAnalyzer:
    """Represents a message analyzer"""

    def __init__(self, message: discord.Message) -> None:
        """
        Initialize a new MessageAnalyzer

        Params:
            message: discord.Message
        """
        self.entity = message
        self.text = message.content
        self.author_id = message.author.id
        self.words = message.content.split()
        self.length = len(message.content)

    @property
    def is_valid(self) -> bool:
        """
        Check is the message passing conditions

        Returns:
            bool
        """
        if (
            self.entity.mentions
            or len(self.words) <= int(environ.get('MA_WORDS_COUNT', '3'))
            or self.length <= int(environ.get('MA_TEXT_LENGTH', 10))
            or str(self.author_id) in environ.get('MA_USERS_BLACKLIST', '').split()
            or '\n' in self.text
        ):
            return False
        return True
