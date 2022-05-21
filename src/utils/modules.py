from .enums import *


class Modules:
    def __init__(self):
        self.modules = []

    @staticmethod
    def create_default_list() -> dict:
        """Creates the default module list for new acc"""
        return {"farm": Farm.BASIC.value, "lab": Lab.BASIC.value, "trading": Trading.BASIC.value}
