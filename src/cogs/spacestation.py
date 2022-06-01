import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import option

from ..modules import LabModule, GreenhouseModule
from ..database import Users


class SpaceStation(commands.Cog):
    def __init__(self, bot):
        print('init run')
        self.bot = bot

    @slash_command()
    @option("level", type=int, description="View the level of a lab module", default=1, min_value=1, max_value=5)
    async def moduleinfo(self, ctx: discord.ApplicationContext, level: str):
        labmod = LabModule(int(level))
        await ctx.respond(embed=labmod.as_embed())

    @slash_command()
    # @option(name="tests", type=str, description="This commands is testing this exact thing", default="a")
    async def test(self, ctx: discord.ApplicationContext, tests: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(["test1", "test3"])), testt: discord.Option(str, choices=["test1", "test3"])):
        await ctx.respond(f"{tests} hm")

    @slash_command()
    async def create_account(self, ctx: discord.ApplicationContext):
        await Users.create(userid=ctx.user.id)
        await ctx.respond("Created account (check db)")


def setup(bot):
    bot.add_cog(SpaceStation(bot))
