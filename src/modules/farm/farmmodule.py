import discord
from src.utils import FiveTier


class FarmModule:
    def __init__(self, name: str, description: str, level: int, crop_gain: list):
        self.name = name
        self.description = description
        self.level = level
        self.crop_gain = crop_gain

    def __repr__(self):
        return f"<FarmModule name={self.name} description={self.description} level={self.level}"

    def level_to_gain(self, level: int | None = None) -> int:
        """Converts the farms level to the amount of crop gain"""
        return self.crop_gain[level - 1 if level is not None else self.level - 1]

    def as_embed(self) -> discord.Embed:
        """Converts the module into an embed"""
        em = discord.Embed(title=self.name,
                           description=f"Level: `{FiveTier(self.level).name}` \nCrop Gain: `{self.level_to_gain()}` \n\n{self.description}",
                           color=discord.Color.blurple())
        return em
