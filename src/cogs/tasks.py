import discord
from discord.ext import commands, tasks
import asyncio

from ..database.models import SpaceStation, Users
from ..utils import to_farm_module, to_science_module


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.farms.start()
        self.labs.start()

    def cog_unload(self):
        self.farms.cancel()
        self.labs.cancel()

    @tasks.loop(minutes=3)
    async def farms(self):
        allstations = await SpaceStation.all()
        for i in allstations:
            for farmlvl in i.modules['farm']:
                module = to_farm_module('greenhouse', farmlvl)
                user = await Users.get_from_spacestation(i.id)

                try:
                    test = int(user.materials.get('crops'))
                except TypeError:
                    user.materials['crops'] = 0

                user.materials['crops'] += module.level_to_gain()
                await user.save()
                await i.save()

    @farms.before_loop
    async def before_farms(self):
        """Wait for the bot to connect and
           for the database conection
           to be established"""
        print('FARMS TASK waiting')

        await self.bot.wait_until_ready()
        await asyncio.sleep(3)

        print('FARMS TASK has started')

    @tasks.loop(minutes=5)
    async def labs(self):
        allstations = await SpaceStation.all()
        for i in allstations:
            for lablvl in i.modules['lab']:
                module = to_science_module('lab', lablvl)
                user = await Users.get_from_spacestation(i.id)

                user.science += module.level_to_gain()
                await user.save()
            await i.save()

    @labs.before_loop
    async def before_labs(self):
        """Wait for the bot to connect and for the database"""
        print('LABS TASK waiting')

        await self.bot.wait_until_ready()
        await asyncio.sleep(3)

        print('LABS TASK started')


def setup(bot):
    bot.add_cog(Tasks(bot))
