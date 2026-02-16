from dataclasses import dataclass

from game import items
from game.api import Tile
from game.base import GameObject


class Backpack:
    def __init__(self):
        self.items: list[items.Item] = []

@dataclass
class Character(GameObject):
    tile: Tile = Tile.CHARACTER
    max_hp: int = 10
    hp: int = max_hp
    str = 3
    dex = 3
    weapon = items.fist
    backpack: Backpack = Backpack()

    @property
    def treasure(self):
        return sum(item.value for item in self.backpack.items if isinstance(item, items.Treasure))


@dataclass
class Monster(GameObject):
    depth: int = 0
    hostility: int = 0
    max_hp: int = 0
    str: int = 0
    dex: int = 0
    treasure: int = 0


@dataclass
class Zombie(Monster):
    tile: Tile = Tile.MONSTER_ZOMBIE

    def __post_init__(self):
        self.dex = int((3 + self.depth) / 5)
        self.str = int((3 + self.depth) / 3)
        self.max_hp = int((3 + self.depth) / 1)
        self.hostility = 5
        self.treasure = self.depth


@dataclass
class Vampire(Monster):
    tile: Tile = Tile.MONSTER_VAMPIRE

    def __post_init__(self):
        self.dex = int(3 + self.depth)
        self.str = int((3 + self.depth) / 3)
        self.max_hp = int((3 + self.depth) / 5)
        self.hostility = 8
        self.treasure = self.depth


@dataclass
class Ghost(Monster):
    tile: Tile = Tile.MONSTER_GHOST

    def __post_init__(self):
        self.dex = int((3 + self.depth) / 1)
        self.str = int((3 + self.depth) / 5)
        self.max_hp = int((3 + self.depth) / 5)
        self.hostility = 3
        self.treasure = self.depth


@dataclass
class Ogre(Monster):
    tile: Tile = Tile.MONSTER_OGRE

    def __post_init__(self):
        self.dex = int((3 + self.depth) / 5)
        self.str = int((3 + self.depth) * 1.5)
        self.max_hp = int((3 + self.depth) * 1.5)
        self.hostility = 5
        self.treasure = self.depth


@dataclass
class SnakeMage(Monster):
    tile: Tile = Tile.MONSTER_SNAKE_MAGE

    def __post_init__(self):
        self.dex = int((3 + self.depth) * 1.5)
        self.str = int((3 + self.depth) / 3)
        self.max_hp = int((3 + self.depth) / 3)
        self.hostility = 8
        self.treasure = self.depth


monster_types = [Zombie, Vampire, Ghost, Ogre, SnakeMage]
