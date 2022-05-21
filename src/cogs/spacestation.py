import discord
from discord.ext import commands
from discord.commands import slash_command
from ..modules.lab import LabModule


class SpaceStation(commands.Cog):
    def __init__(self, bot):
        print('init run')
        self.bot = bot

    @slash_command(guild_ids=[801646969676234782])
    async def moduleinfo(self, ctx: discord.ApplicationContext):
        labmod = LabModule(1)
        await ctx.respond(embed=labmod.as_embed())

    @slash_command(guild_ids=[801646969676234782])
    async def test(self, ctx: discord.ApplicationContext):
        await ctx.respond("OS OK")


def setup(bot):
    bot.add_cog(SpaceStation(bot))
