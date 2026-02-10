from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class Tile(Enum):
    WALL_V = "\u2503"
    WALL_H = "\u2501"
    CORNER_TL = "\u250f"
    CORNER_TR = "\u2513"
    CORNER_BL = "\u2517"
    CORNER_BR = "\u251b"
    FLOOR = "."
    CHARACTER = "@"
    CORRIDOR = "#"
    ITEM_WEAPON = "/"
    ITEM_ELIXIR = "!"
    ITEM_SCROLL = "%"
    ITEM_FOOD = "*"
    UNKNOWN = "?"
    STAIR = ">"
    MONSTER_ZOMBIE = "z"
    MONSTER_VAMPIRE = "v"
    MONSTER_GHOST = "g"
    MONSTER_OGRE = "o"
    MONSTER_SNAKE_MAGE = "s"


class InputEvent(Enum):
    MOVE_UP = "w"
    MOVE_DOWN = "s"
    MOVE_LEFT = "a"
    MOVE_RIGHT = "d"


@dataclass(frozen=True)
class DrawTile:
    x: int
    y: int
    tile: Tile


@dataclass(frozen=True)
class Frame:
    tiles: Iterable[DrawTile]
    hp: int
    max_hp: int
    treasure: int
    level: int
