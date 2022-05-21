from tortoise import fields
from tortoise.models import Model
from src.utils import Modules


class SpaceStation(Model):
    id = fields.BigIntField(pk=True)
    user = fields.ForeignKeyField('bot.Users')
    modules = fields.JSONField(default=Modules.create_default_list())
    science = fields.BigIntField(default=0)


class Users(Model):
    id = fields.BigIntField(pk=True)
    userid = fields.BigIntField(unique=True)
    materials = fields.JSONField(default=[])
    blueprints = fields.JSONField(default=[])
    money = fields.JSONField(default=0)
