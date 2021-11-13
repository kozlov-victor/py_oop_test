from consts import WIDTH, HEIGHT
from lake_controller import LakeController
from models.fishes import PredatorFish, PrayFish
import random,time


clear_console = lambda: print('\n' * 150)

lake_controller = LakeController(30, 10)
for i in range(1, 30):
    r = random.randint(0, 10)
    if r > 5:
        f = PredatorFish(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        f = PrayFish(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    lake_controller.add_fish(f)

for i in range(0, 100):
    clear_console()
    lake_controller.next_tick()
    lake_controller.debug()
    time.sleep(1)
