from tortoise import fields
from tortoise.models import Model
from ..utils import Modules


class SpaceStation(Model):
    id = fields.BigIntField(pk=True)
    level = fields.IntField(default=1)
    modules = fields.JSONField(default=Modules.create_default_list())


class Users(Model):
    id = fields.BigIntField(pk=True)
    userid = fields.BigIntField(unique=True)
    materials = fields.JSONField(default={})
    blueprints = fields.JSONField(default={})
    money = fields.JSONField(default=0)
    science = fields.BigIntField(default=0)
    spacestation = fields.ForeignKeyField('bot.SpaceStation')

    @classmethod
    async def create(cls, **kwargs):
        """
        Creates a User and SpaceStation in the database.

        :param kwargs: The arguments for creating the User
        :return: The Users Model
        """
        spacestation = await SpaceStation.create()
        return await super(Users, cls).create(spacestation=spacestation, **kwargs)

    @classmethod
    async def get_science(cls, userid: int) -> int:
        """
        Gets the amount of science a user has. If the provided
        userid is not in the db it is created.

        :param userid: The userid to search for.
        :return: The amount of science the user has.
        """
        return (await cls.get_or_create(userid=userid))[0].science

    @classmethod
    async def get_money(cls, userid: int) -> int:
        """
        Gets the amount of money a user has. If the provided
        userid is not in the db it is created.

        :param userid: The userid to search for.
        :return: The amount of money the user has.
        """
        return (await cls.get_or_create(userid=userid))[0].money

    @classmethod
    async def get_spacestation_lvl(cls, userid: int) -> int:
        """
        Gets the users curren spacestation level. If the
        provided userid is not in the db it is created.

        :param userid: The userid to search for.
        :return: The spacestation level the user has.
        """
        userinfo = (await cls.get_or_create(userid=userid))[0]
        spacestation = await userinfo.spacestation

        return spacestation.level

    @classmethod
    async def get_materials(cls, userid: int) -> dict:
        """
        Gets the materials the user has. If the provided
        userid is not in the db it is created.

        :param userid: The userid to search for.
        :return: The materials the user has.
        """
        return (await cls.get_or_create(userid=userid))[0].materials

    @classmethod
    async def get_blueprints(cls, userid: int) -> list:
        """
        Gets the blueprints the user has. If the provided
        userid is not in the db it is created

        :param userid: The userid to search for.
        :return: The blueprints the user has.
        """
        return (await cls.get_or_create(userid=userid))[0].blueprints

    @classmethod
    async def get_user_info(cls, userid: int):
        """
        Gets all the user info in the db. If the
        provided userid is not in the db it is created.

        :param userid: The userid to search for.
        :return: The users info.
        """
        return (await cls.get_or_create(userid=userid))[0]
