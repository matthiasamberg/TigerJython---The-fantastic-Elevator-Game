import random


class SeededRandom:
    def __init__(self, seed):
        self.nextSeed = seed

    def getRandom(self):
        random.seed(self.nextSeed)
        self.nextSeed = random.random()
        return random.random()

    def getRandInt(self, low, high):
        random.seed(self.nextSeed)
        self.nextSeed = random.random()
        return random.randint(low, high)
