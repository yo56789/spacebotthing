from .enums import ThreeTier, FiveTier


class Modules:
    def __init__(self):
        self.modules = []

    @staticmethod
    def create_default_list() -> dict:
        """Creates the default module list for new acc"""
        return {"farm": [FiveTier.BASIC.value], "lab": [FiveTier.BASIC.value], "trading": [ThreeTier.BASIC.value]}

