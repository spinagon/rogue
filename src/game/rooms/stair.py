from dataclasses import dataclass
from game.base import GameObject
from api import Tile


@dataclass
class Stair(GameObject):
    tile: Tile = Tile.STAIR