from .sciencemodule import ScienceModule


class LabModule(ScienceModule):
    def __init__(self, level: int):
        self.name = "Lab Module"
        self.description = "Produces science that can be used to unlock new blueprints!"
        self.level = level
        # basic - advanced - elite - ultimate - superior
        self.science_gain = [1, 3, 9, 18, 36]

        super(LabModule, self).__init__(self.name, self.description, self.level, self.science_gain)
