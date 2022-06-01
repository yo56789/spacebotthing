import discord
from discord.ext import commands
from discord.commands import slash_command, SlashCommandGroup

from ..utils import buy, to_miner_module
from ..database import SpaceStation


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    shop = SlashCommandGroup("shop", "Used to buy various items to improve your space station!")

    @shop.command()
    async def modules(self, ctx: discord.ApplicationContext, module: discord.Option(int, description="The module to be purchased", choices=[discord.OptionChoice("BASIC Miner Module", 1)])):
        modname = ""
        print(await SpaceStation.all())
        if module == 1:
            module = to_miner_module("miner", 1)
            modname = "miner"

        em, ephemeral = await buy("module", modname, module.level, module.cost, ctx.author.id)

        await ctx.respond(embed=em, ephemeral=ephemeral)


def setup(bot):
    bot.add_cog(Economy(bot))
