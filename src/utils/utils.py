from ..modules import *
from ..database import Users


def format_materials(materials: dict) -> str:
    """

    :param materials: The dict of materials to be formatted.
    :return: The formatted dict as a string.
    """
    returnstr = ""
    for i in materials:
        returnstr += f"**{i.title()}** - `{materials[i]}` \n"

    return returnstr


def format_blueprints(blueprints: list) -> str:
    """
    Formats it the provided list.

    :param blueprints: The list of blueprints to be formatted.
    :return: The formatted list as a string.
    """
    returnstr = ""
    for i in blueprints:
        returnstr += f"**{i.title()}** \n"

    return returnstr


def format_ore(ores: list) -> str:
    """
    Formats the provided list.

    :param ores: The ores to format.
    :return: The formmated ores as a string.
    """
    returnstr = ""
    for i in ores:
        returnstr += f"**{i.title()}** "

    return returnstr


def to_farm_module(module: str, level: int) -> ...:
    """
    Converts a farm modules name and level its class.

    :param module: Name of the module.
    :param level: The modules level.
    :return: The class of the module.
    """
    if module == "greenhouse":
        return GreenhouseModule(level)


def to_science_module(module: str, level: int) -> ...:
    """
    Converts a science modules name and level to its class.

    :param module: Name of the module.
    :param level: The modules level.
    :return: The class of the module.
    """
    if module == "lab":
        return LabModule(level)


def to_miner_module(module: str, level: int) -> ...:
    """
    Converts a miner modules name and level to its class.

    :param module: Name of the module.
    :param level: Level of the module.
    :return: The class of the module
    """
    if module == "miner":
        return MinerModule(level)


def assemble_error_embed(description: str) -> discord.Embed:
    """
    Creates an embed with the given description

    :param description: Text to put in the `description` part of an embed
    :return: The created embed
    """
    return discord.Embed(title="Oop",
                         description=description,
                         color=discord.Color.red())


def assemble_success_embed(title: str, description: str) -> discord.Embed:
    """
    Creates an embed with the given description

    :param title: The title of the embed
    :param description: Description of the embed
    :return: The created embed
    """
    return discord.Embed(title=title,
                         description=description,
                         color=discord.Color.green())


async def buy(category: str, itemname: str, itemlevel: str, cost: int, userid: int) -> (discord.Embed, bool):
    """
    Purchases an item for the user

    :param category: The category that the item is in the db
    :param itemname: The name of the item
    :param itemlevel: The level of the item
    :param cost: The amount of money needed to purchase
    :param userid: The user who is purchasing item's id
    :return: An embed and a bool for ephemeral responses
    """
    match category:
        case "module":
            user = await Users.get_user_info(userid=userid)
            spacestation = await Users.get_spacestation(userid=userid)
            if cost > user.money:
                return assemble_error_embed("You do not have sufficent funds to purchase this item!"), True

            try:
                if len(spacestation.modules.get(itemname)) == 5:
                    return assemble_error_embed("You have purchased the maximum amount of this module!"), True
            except TypeError:
                spacestation.modules[itemname] = []

            user.money -= cost
            spacestation.modules[itemname].append(int(itemlevel))

            await user.save()
            await spacestation.save()
            return assemble_success_embed("Purchase Successful!",
                                          f"You have successfully purchased a **{itemname} module** \nYou now have `${user.money}`"), False

        case _:
            return assemble_error_embed("Something went terribly wrong! Try again later."), True
