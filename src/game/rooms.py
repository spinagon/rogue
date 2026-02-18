import logging
import math
import random

from game import constants

logger = logging.getLogger(__name__)


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

    def is_floor(self, x, y):
        return self.is_inside(x, y) and not self.is_wall(x, y)

    def is_wall(self, x, y):
        return self.is_inside(x, y) and (
            x in [self.x0, self.x1] or y in [self.y0, self.y1]
        )

    def is_inside(self, x, y):
        return self.x0 <= x <= self.x1 and self.y0 <= y <= self.y1


class Corridor:
    def __init__(self, rooms):
        self.rooms = sorted(rooms, key=lambda x: x.id)
        if self.rooms[1].id - self.rooms[0].id == 1:
            self.horizontal = True
            self.x0 = self.rooms[0].x1
            self.x1 = self.rooms[1].x0
            self.y0 = random.randint(self.rooms[0].y0 + 1, self.rooms[0].y1 - 1)
            self.y1 = random.randint(self.rooms[1].y0 + 1, self.rooms[1].y1 - 1)
        else:
            self.horizontal = False
            self.y0 = self.rooms[0].y1
            self.y1 = self.rooms[1].y0
            self.x0 = random.randint(self.rooms[0].x0 + 1, self.rooms[0].x1 - 1)
            self.x1 = random.randint(self.rooms[1].x0 + 1, self.rooms[1].x1 - 1)

    def is_inside(self, x, y):
        if in_range(x, self.x0, self.x1) and in_range(y, self.y0, self.y1):
            if self.horizontal:
                if x == self.x0 and y != self.y0:
                    return False
                if x == self.x1 and y != self.y1:
                    return False
                if y == self.y0 and abs(x - self.x0) == 1:
                    return True
                if y == self.y1 and abs(x - self.x1) == 1:
                    return True
            else:
                if y == self.y0 and x != self.x0:
                    return False
                if y == self.y1 and x != self.x1:
                    return False
                if x == self.x0 and abs(y - self.y0) == 1:
                    return True
                if x == self.x1 and abs(y - self.y1) == 1:
                    return True

            dist = distance_to_line((self.x0, self.y0), (self.x1, self.y1), (x, y))
            if dist <= 0.71:
                return True
        return False


def distance_to_line(p0, p1, p) -> float:
    x0, y0 = p0
    x1, y1 = p1
    x, y = p
    return abs((y1 - y0) * x - (x1 - x0) * y + x1 * y0 - y1 * x0) / math.sqrt(
        (y1 - y0) ** 2 + (x1 - x0) ** 2
    )


def in_range(x, x0, x1):
    return min(x0, x1) <= x <= max(x0, x1)
