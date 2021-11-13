from consts import LEFT, RIGHT, UP, DOWN, WIDTH, HEIGHT
import random


def dist(x1: int, y1: int, x2: int, y2: int):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5


def clamp(val: int, min: int, max: int) -> int:
    if val < min:
        return min
    if val > max:
        return max
    return val


class AbstractFish:
    def __init__(self, x: int, y: int):
        self.ticks = 0
        self.x = x
        self.y = y

    def _move_by(self, x: int, y: int):
        self.x = clamp(self.x + x,0,WIDTH-1)
        self.y = clamp(self.y + y,0,HEIGHT-1)

    def move_to_direction_by(self, direction: int, by: int):
        if direction == LEFT:
            self._move_by(-by, 0)
        if direction == RIGHT:
            self._move_by(by, 0)
        if direction == UP:
            self._move_by(0, -by)
        if direction == DOWN:
            self._move_by(0, by)


class PredatorFish(AbstractFish):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    def get_direction_to_closest_prey(self, prays: list) -> int:
        closest_prey = prays[0]
        dist_to_closest = -10000
        for p in prays:
            dist_to_current = dist(self.x, self.y, p.x, p.y)
            if dist_to_current < dist_to_closest:
                dist_to_closest = dist_to_current
                closest_prey = p
        points_to_move_by_x = closest_prey.x - self.x
        points_to_move_by_y = closest_prey.y - self.y
        dir1 = RIGHT if points_to_move_by_x > 0 else LEFT
        dir2 = DOWN if points_to_move_by_y > 0 else UP
        return dir1 if random.randint(0, 10) > 5 else dir2


class PrayFish(AbstractFish):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
