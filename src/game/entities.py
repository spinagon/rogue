import random
from dataclasses import dataclass

from game import items
from game.api import Tile
from game.base import GameObject


class Backpack:
    def __init__(self):
        self.items: list[items.Item] = []


class Entity(GameObject):
    tile: Tile
    max_hp: int
    max_hp_mod = 0
    hp: int
    str: int
    str_mod = 0
    dex: int
    dex_mod = 0
    weapon = items.fist
    name: str = "unknown"


@dataclass
class Character(Entity):
    tile: Tile = Tile.CHARACTER
    max_hp: int = 10
    hp: int = max_hp
    str = 3
    dex = 3
    weapon = items.fist
    backpack: Backpack = Backpack()
    name = "player"

    @property
    def treasure(self):
        return sum(
            item.value
            for item in self.backpack.items
            if isinstance(item, items.Treasure)
        )


@dataclass
class Monster(Entity):
    depth: int = 0
    hostility: int = 0
    max_hp: int = 0
    str: int = 0
    dex: int = 0
    hp: int = 0
    name = "monster"

    @property
    def treasure(self):
        return random.randint(1, self.hostility + self.max_hp + self.str + self.dex)

    def get_move(self):
        return random.choice(
            [
                [0, 1],
                [0, -1],
                [1, 0],
                [-1, 0],
            ]
        )


@dataclass
class Zombie(Monster):
    tile: Tile = Tile.MONSTER_ZOMBIE
    name = "zombie"

    def __post_init__(self):
        self.dex = int((3 + self.depth) / 5)
        self.str = int((3 + self.depth) / 3)
        self.max_hp = int((3 + self.depth) / 1)
        self.hp = self.max_hp
        self.hostility = 5


@dataclass
class Vampire(Monster):
    tile: Tile = Tile.MONSTER_VAMPIRE
    name = "vampire"

    def __post_init__(self):
        self.dex = int(3 + self.depth)
        self.str = int((3 + self.depth) / 3)
        self.max_hp = int((3 + self.depth) / 5)
        self.hp = self.max_hp
        self.hostility = 8


@dataclass
class Ghost(Monster):
    tile: Tile = Tile.MONSTER_GHOST
    name = "ghost"

    def __post_init__(self):
        self.dex = int((3 + self.depth) / 1)
        self.str = int((3 + self.depth) / 5)
        self.max_hp = int((3 + self.depth) / 5)
        self.hp = self.max_hp
        self.hostility = 3


@dataclass
class Ogre(Monster):
    tile: Tile = Tile.MONSTER_OGRE
    name = "ogre"

    def __post_init__(self):
        self.dex = int((3 + self.depth) / 5)
        self.str = int((3 + self.depth) * 1.5)
        self.max_hp = int((3 + self.depth) * 1.5)
        self.hp = self.max_hp
        self.hostility = 5


@dataclass
class SnakeMage(Monster):
    tile: Tile = Tile.MONSTER_SNAKE_MAGE
    name = "snake mage"

    def __post_init__(self):
        self.dex = int((3 + self.depth) * 1.5)
        self.str = int((3 + self.depth) / 3)
        self.max_hp = int((3 + self.depth) / 3)
        self.hp = self.max_hp
        self.hostility = 8


monster_types = [Zombie, Vampire, Ghost, Ogre, SnakeMage]
