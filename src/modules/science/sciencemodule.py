import discord
from src.utils import FiveTier


class ScienceModule:
    def __init__(self, name: str, description: str, level: int, science_gain: list):
        """
        Parent class for all science generating modules.

        :param name: Display name of the module.
        :param description: Information about the module.
        :param level: The current modules level.
        :param science_gain: The amount of science per level the module creates.
        """
        self.name = name
        self.description = description
        self.level = level
        self.science_gain = science_gain

    def __repr__(self):
        return f"<ScienceModule name={self.name} description={self.description} level={self.level}>"

    def level_to_gain(self, level: int | None = None) -> int:
        """
        The amount of science that will be gained from the level.

        :param level: The level of the module.
        :return: The amount of science that will be gained.
        """
        return self.science_gain[level - 1 if level is not None else self.level - 1]

    def as_embed(self) -> discord.Embed:
        """
        Converts the modules info into an embed.

        :return: The embed
        """
        em = discord.Embed(title=self.name,
                           description=f"Level: `{FiveTier(self.level).name}`\nScience Gain: `{self.level_to_gain()}` \n\n{self.description}",
                           color=discord.Color.blurple())
        return em
