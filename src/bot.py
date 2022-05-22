import discord
from discord import option
from discord.ext import commands
from tortoise import Tortoise

import os
import dotenv

dotenv.load_dotenv()

bot = commands.Bot(intents=discord.Intents.all())


@bot.slash_command(guild_ids=[801646969676234782])
@option("cog", description="The cog to reload", default="spacestation")
async def reload(ctx, cog: str):
    # RELOADS A COG ONLY FOR DEV
    bot.reload_extension(f'src.cogs.{cog}')
    await ctx.respond(f"reloaded: {cog}", ephemeral=True)


@bot.event
async def on_ready():
    # Connect to the sqlite database using tortoise ORM
    config = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.sqlite",
                "credentials": {
                    "file_path": os.getcwd() + "/database/data.db"
                }
            }
        },
        "apps": {
            "bot": {"models": ["src.database.models"]}
        }
    }

    await Tortoise.init(config)
    await Tortoise.generate_schemas()

    print("Bot has connected")

# LOAD ALL COGS
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        print(file)
        bot.load_extension(f'src.cogs.{file[:-3]}')

if __name__ == "__main__":
    _token = os.getenv("TOKEN")
    bot.run(_token)
