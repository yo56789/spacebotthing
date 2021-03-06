from .farmmodule import FarmModule


class GreenhouseModule(FarmModule):
    def __init__(self, level: int):
        """
        Greenhouse module subclass of FarmModule.

        :param level: The level of the module.
        """
        self.name = "Farm"
        self.description = "Produces crops that can be used to create food and earn money!"
        self.level = level
        # basic - advanced - elite - ultimate - special
        self.crop_gain = [3, 9, 18, 36, 48]
        # elite - ultimate - special
        self.recipe = {"3": {}}
        super().__init__(self.name, self.description, self.level, self.crop_gain)
