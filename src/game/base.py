from dataclasses import dataclass, KW_ONLY

from game.api import Tile


@dataclass
class GameObject:
    _: KW_ONLY
    x: int = -1
    y: int = -1
    tile: Tile = Tile.UNKNOWN

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def place(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
