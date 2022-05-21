import discord


class ScienceModule:
    def __init__(self, name: str, description: str, level: int, science_gain: list):
        self.name = name
        self.description = description
        self.level = level
        self.science_gain = science_gain

    def __repr__(self):
        return f"<ScienceModule name={self.name} description={self.description} level={self.level}>"

    def level_to_gain(self, level: int | None = None) -> int:
        """Converts the labs level to the amount of science gain"""
        return self.science_gain[level - 1 if level is not None else self.level - 1]

    def as_embed(self) -> discord.Embed:
        """Converts the module into an info embed"""
        em = discord.Embed(title=self.name,
                           description=f"Current Science Gain: {self.level_to_gain()} \n\n{self.description}",
                           color=discord.Color.blurple())
        return em
