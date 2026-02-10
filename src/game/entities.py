from dataclasses import dataclass

from game import items
from game.api import Tile
from game.base import GameObject


@dataclass
class Character(GameObject):
    tile: Tile = Tile.CHARACTER
    max_hp: int = 10
    str = 3
    dex = 3
    weapon = items.fist

    def __post_init__(self, x, y):
        super().__post_init__(x, y)
        self.hp = self.max_hp


@dataclass
class Monster(GameObject):
    pass


@dataclass
class Zombie(Monster):
    level: int = 0
    tile: Tile = Tile.MONSTER_ZOMBIE

    def __post_init__(self, x, y):
        super().__post_init__(x, y)
        self.dex = int((3 + self.level) / 5)
        self.str = int((3 + self.level) / 3)
        self.max_hp = int((3 + self.level) / 1)
        self.hostility = 5
        self.treasure = self.level


@dataclass
class Vampire(Monster):
    level: int = 0
    tile: Tile = Tile.MONSTER_VAMPIRE

    def __post_init__(self, x, y):
        super().__post_init__(x, y)
        self.dex = int(3 + self.level)
        self.str = int((3 + self.level) / 3)
        self.max_hp = int((3 + self.level) / 5)
        self.hostility = 8
        self.treasure = self.level


@dataclass
class Ghost(Monster):
    level: int = 0
    tile: Tile = Tile.MONSTER_GHOST

    def __post_init__(self, x, y):
        super().__post_init__(x, y)
        self.dex = int((3 + self.level) / 1)
        self.str = int((3 + self.level) / 5)
        self.max_hp = int((3 + self.level) / 5)
        self.hostility = 3
        self.treasure = self.level


@dataclass
class Ogre(Monster):
    level: int = 0
    tile: Tile = Tile.MONSTER_OGRE

    def __post_init__(self, x, y):
        super().__post_init__(x, y)
        self.dex = int((3 + self.level) / 5)
        self.str = int((3 + self.level) * 1.5)
        self.max_hp = int((3 + self.level) * 1.5)
        self.hostility = 5
        self.treasure = self.level


@dataclass
class SnakeMage(Monster):
    level: int = 0
    tile: Tile = Tile.MONSTER_SNAKE_MAGE

    def __post_init__(self, x, y):
        super().__post_init__(x, y)
        self.dex = int((3 + self.level) * 1.5)
        self.str = int((3 + self.level) / 3)
        self.max_hp = int((3 + self.level) / 3)
        self.hostility = 8
        self.treasure = self.level


monster_types = [Zombie, Vampire, Ghost, Ogre, SnakeMage]
