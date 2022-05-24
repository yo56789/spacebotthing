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
