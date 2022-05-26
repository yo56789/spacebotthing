import discord

from src.utils import FiveTier


class FarmModule:
    def __init__(self, name: str, description: str, level: int, crop_gain: list, recipes: dict):
        """
        Parent class for all crop generating modules.

        :param name: Display name of the module.
        :param description: Information about the module.
        :param level: Current modules level.
        :param crop_gain: The amount of crops per level the module creates
        """
        self.name = name
        self.description = description
        self.level = level
        self.crop_gain = crop_gain
        self.recipes = recipes

    def __repr__(self):
        return f"<FarmModule name={self.name} description={self.description} level={self.level}"

    def level_to_gain(self, level: int | None = None) -> int:
        """
        The amount of crops that will be gained from the level.

        :param level: The level of the module.
        :return: The amount of crops that will be gained.
        """
        return self.crop_gain[level - 1 if level is not None else self.level - 1]

    def as_embed(self) -> discord.Embed:
        """
        Converts the module info into an embed

        :return: The embed
        """
        em = discord.Embed(title=self.name,
                           description=f"Level: `{self.level} - {FiveTier(self.level).name}` \nCrop Gain: `{self.level_to_gain()}` \n\n{self.description}",
                           color=discord.Color.blurple())
        return em
