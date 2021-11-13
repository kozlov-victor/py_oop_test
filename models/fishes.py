class _AbstractFish:
    def __init__(self):
        self.ticks = 0
        self.x = 0
        self.y = 0


class PredatorFish(_AbstractFish):
    def __init__(self):
        super.__init__()


class PrayFish(_AbstractFish):
    def __init__(self):
        super.__init__()
