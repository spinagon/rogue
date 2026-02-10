from dataclasses import dataclass, field, InitVar, KW_ONLY

from game.api import Tile


@dataclass
class GameObject:
    _: KW_ONLY
    x: InitVar[int] = -1
    y: InitVar[int] = -1
    _x: int = field(init=False, default=0)
    _y: int = field(init=False, default=0)
    tile: Tile = Tile.UNKNOWN

    def __post_init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
