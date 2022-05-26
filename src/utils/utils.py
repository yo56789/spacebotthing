from ..modules import *


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

#
# def to_module(category: str, module: str, level: int) -> ...:
#     """
#     Converts a module name and level to the class of
#     the specified module.
#
#     :param category: Parent class name of the module
#     :param module: Name of the module.
#     :param level: Modules level.
#     :return: Class of the module.
#     """
#     match category:
#         case "farm":
#             if module == "greenhouse":
#                 return GreenhouseModule(level)
#         case "science":
#             if module == "lab":
#                 return LabModule(level)
#         case _:
#             raise KeyError("Could not find the specified category")


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
