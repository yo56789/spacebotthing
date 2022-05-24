import discord
from discord.ext import commands
from discord.commands import slash_command

from ..database import Users
from ..utils import format_materials, format_blueprints


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[801646969676234782])
    async def profile(self, ctx: discord.ApplicationContext):
        user = (await Users.get_or_create(userid=ctx.user.id))[0]
        spacestationlvl = await Users.get_spacestation_lvl(userid=ctx.author.id)

        embed = discord.Embed(title=ctx.author.name,
                              description=f"**Money:** `${user.money}`\n**Science:** `{user.science}` \n**Space Station Level:** `{str(spacestationlvl)}`",
                              color=discord.Color.dark_purple())
        embed.set_footer(text="YoSpace was made by .Yo!")

        await ctx.respond(embed=embed)

    @slash_command(guild_ids=[801646969676234782])
    async def money(self, ctx: discord.ApplicationContext):
        money = await Users.get_money(userid=ctx.author.id)

        await ctx.respond(f"You have `${money}`", ephemeral=True)

    @slash_command(guild_ids=[801646969676234782])
    async def science(self, ctx: discord.ApplicationContext):
        science = await Users.get_science(userid=ctx.author.id)
        await ctx.respond(f"You have `{science}` science", ephemeral=True)

    @slash_command(guild_ids=[801646969676234782])
    async def spacestationlevel(self, ctx: discord.ApplicationContext):
        lvl = await Users.get_spacestation_lvl(userid=ctx.author.id)

        await ctx.respond(f"Your space station level is `{lvl}`", ephemeral=True)

    @slash_command(guild_ids=[801646969676234782])
    async def materials(self, ctx: discord.ApplicationContext):
        materials = await Users.get_materials(userid=ctx.author.id)
        if len(materials) == 0:
            return await ctx.respond("You do not have any materials. Materials are gained from farms and miners!", ephemeral=True)
        em = discord.Embed(title="Materials",
                           description=f"{format_materials(materials)}",
                           color=discord.Color.blurple())
        em.set_footer(text="Use /material <material> to get more info on a material!")

        await ctx.respond(embed=em, ephemeral=True)

    @slash_command(guild_ids=[801646969676234782])
    async def blueprints(self, ctx: discord.ApplicationContext):
        blueprints = await Users.get_blueprints(userid=ctx.author.id)
        if len(blueprints) == 0:
            return await ctx.respond("You don't have any blueprints. Blueprints can be obtained with science using `/blueprint`!", ephemeral=True)
        em = discord.Embed(title="Blueprints",
                           description=f"{format_blueprints(blueprints)}",
                           color=discord.Color.blurple())
        em.set_footer(text="Blueprints are used to construct upgrades!")

        await ctx.respond(embed=em, ephemeral=True)


def setup(bot):
    bot.add_cog(User(bot))
