from models.lake import Lake

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4


class PoolController:
    def __init__(self):
        self.lake = Lake(40,10)
        self.predators = []
        self.preys = []

    def debug(self):
        info = self.lake.debug()
        print(info)
