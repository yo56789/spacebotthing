import discord
from discord.ext import commands
from discord.commands import slash_command, SlashCommandGroup

from ..utils import to_farm_module, to_science_module, to_miner_module, format_ore, OreTier
from ..modules import MinerModule


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    module = SlashCommandGroup("module", "Get information about a module and its level")

    # @slash_command(guild_ids=[801646969676234782])
    # async def module(self, ctx: discord.ApplicationContext, category: discord.Option(str, choices=["farm", "science"]), module: discord.Option(str, choices=["greenhouse", "lab"]), level: discord.Option(int, min_value=1, max_value=5)):
    #     mod = to_module(category, module, level)
    #
    #     await ctx.respond(embed=mod.as_embed())

    @module.command()
    async def science(self, ctx: discord.ApplicationContext, module: discord.Option(str, description="The modules name", choices=["lab"]), level: discord.Option(int, description="The level of the module", min_value=1, max_value=5)):
        science_module = to_science_module(module, level)

        await ctx.respond(embed=science_module.as_embed())

    @module.command()
    async def farm(self, ctx: discord.ApplicationContext, module: discord.Option(str, description="The modules name", choices=["greenhouse"]), level: discord.Option(int, description="The level of the module", min_value=1, max_value=5)):
        farm_module = to_farm_module(module, level)

        await ctx.respond(embed=farm_module.as_embed())

    @module.command()
    async def miner(self, ctx: discord.ApplicationContext, module: discord.Option(str, description="The modules name", choices=["miner"]), level: discord.Option(int, description="The level of the module", min_value=1, max_value=3)):
        miner_module = to_miner_module(module, level)

        await ctx.respond(embed=miner_module.as_embed())

    @slash_command()
    async def ore(self, ctx: discord.ApplicationContext, tier: discord.Option(int, description="The tier of ore", choices=[discord.OptionChoice("small", 1), discord.OptionChoice("medium", 2), discord.OptionChoice("large", 3)])):
        module = MinerModule(tier)

        em = discord.Embed(title=f"{OreTier(module.level).name.lower().title()} Asteroids",
                           description=format_ore(module.level_to_ore()),
                           color=discord.Color.blurple())

        await ctx.respond(embed=em, ephemeral=True)


def setup(bot):
    bot.add_cog(Info(bot))
