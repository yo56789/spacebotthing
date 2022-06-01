import discord
from src.utils import ThreeTier, OreTier


class MinerModule:
    def __init__(self, level: int):
        self.name = "Asteroid Miner"
        self.description = "Mines asteroids for ores!"
        self.level = level
        self.cost = 40
        self.recipe = {"2": {}, "3": {}}

    def __repr__(self):
        return f"<MinerModule name={self.name} description={self.description} level={self.level}>"

    def level_to_ore(self) -> list[str]:
        """
        Converts the miners' level to the ore that can be mined

        :return: The ore that can be mined
        """
        match self.level:
            case 1:
                return ["copper", "iron", "coal", "tungsten"]
            case 2:
                return ["copper", "iron", "coal", "tungsten", "titanium", "silicon"]
            case _:
                return ["copper", "iron", "coal", "tungsten", "titanium", "silicon", "gold"]

    def as_embed(self) -> discord.Embed:
        """
        Converts the modules' info to an Embed

        :return: The formmated Embed
        """
        em = discord.Embed(title=f"{ThreeTier(self.level).name} - {self.name}",
                           description=f"level: `{self.level}` \n ore tier: `{OreTier(self.level).name}` \n\n{self.description}",
                           color=discord.Color.blurple())
        em.set_footer(text="Use /ore <tier> to see the ores you get with that tier!")

        return em
