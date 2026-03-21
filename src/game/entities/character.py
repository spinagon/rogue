from dataclasses import dataclass

from api import Tile
from game.items.item import Item
from game.items.treasure import Treasure
from game.items import fist
from dataclasses import dataclass
from game.entities.entity import Entity


class Backpack:
    def __init__(self):
        self.items: list[Item] = []

    def remove(self, item):
        self.items.remove(item)


@dataclass
class Character(Entity):
    tile: Tile = Tile.CHARACTER
    max_hp: int = 10
    hp: int = max_hp
    str = 3
    dex = 3
    weapon = fist
    backpack: Backpack = Backpack()
    name = "player"

    @property
    def treasure(self):
        return sum(
            item.value for item in self.backpack.items if isinstance(item, Treasure)
        )
