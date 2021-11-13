from models.fishes import AbstractFish, PrayFish, PredatorFish
import random

def get_random_direction():
    return random.randint(1, 4)


class LakeController:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.predators = []
        self.preys = []

    def add_fish(self, f: AbstractFish):
        if isinstance(f,PrayFish):
            self.preys.append(f)
        else:
            self.predators.append(f)

    def get_fish_at(self, x: int, y: int):
        for p in self.predators:
            if p.x == x and p.y == y:
                return p
        for p in self.preys:
            if p.x == x and p.y == y:
                return p
        return None

    def next_tick(self):
        for p in self.preys:
            direction = get_random_direction()
            p.move_to_direction_by(direction,1)
            p.ticks += 1
        for p in self.predators:
            direction = p.get_direction_to_closest_prey(self.preys)
            p.move_to_direction_by(direction,1)
            p.ticks += 1


    def debug(self):
        result = ''
        for y in range(0, self.height):
            for x in range(0, self.width):
                fish = self.get_fish_at(x, y)
                if not fish:
                    result += '[ ]'
                elif isinstance(fish, PrayFish):
                    result += '[+]'
                else:
                    result += '[🦈]'
            result += '\n'
        print(result)
