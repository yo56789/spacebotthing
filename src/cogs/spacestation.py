import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import option

from ..modules import LabModule, GreenhouseModule


class SpaceStation(commands.Cog):
    def __init__(self, bot):
        print('init run')
        self.bot = bot

    @slash_command(guild_ids=[801646969676234782])
    @option("level", type=int, description="View the level of a lab module", default=1, min_value=1, max_value=5)
    async def moduleinfo(self, ctx: discord.ApplicationContext, level: str):
        labmod = LabModule(int(level))
        await ctx.respond(embed=labmod.as_embed())

    @slash_command(guild_ids=[801646969676234782])
    async def test(self, ctx: discord.ApplicationContext):
        await ctx.respond("OS OK")


def setup(bot):
    bot.add_cog(SpaceStation(bot))
