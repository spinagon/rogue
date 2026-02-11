import random

from game import constants


class Room:
    def __init__(self, id: int):
        self.id = id
        self.discovered = False
        x = (id % 3) * (constants.LEVEL_WIDTH // 3)
        y = (id // 3) * (constants.LEVEL_HEIGHT // 3)
        self.x0 = random.randint(x + 1, x + constants.LEVEL_WIDTH // 3 - 7)
        self.y0 = random.randint(y + 1, y + constants.LEVEL_HEIGHT // 3 - 5)
        self.x1 = random.randint(self.x0 + 5, x + constants.LEVEL_WIDTH // 3 - 1)
        self.y1 = random.randint(self.y0 + 3, y + constants.LEVEL_HEIGHT // 3 - 1)
