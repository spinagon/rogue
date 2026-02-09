from game import items
from game.api import Tile


class Entity:
    pass


class Character(Entity):
    def __init__(self):
        self.tile = Tile.CHARACTER
        self.max_hp = 10
        self.hp = self.max_hp
        self.str = 3
        self.dex = 3
        self.weapon = items.fist
        self.x = 10
        self.y = 10
        self.treasure = 0


class Monster(Entity):
    pass


class Zombie(Monster):
    def __init__(self, level, x, y):
        self.x = x
        self.y = y
        self.tile = Tile.MONSTER_ZOMBIE
        self.dex = int((3 + level) / 5)
        self.str = int((3 + level) / 3)
        self.max_hp = int((3 + level) / 1)
        self.hostility = 5
        self.treasure = level


class Vampire(Monster):
    def __init__(self, level, x, y):
        self.x = x
        self.y = y
        self.tile = Tile.MONSTER_VAMPIRE
        self.dex = int(3 + level)
        self.str = int((3 + level) / 3)
        self.max_hp = int((3 + level) / 5)
        self.hostility = 8
        self.treasure = level


class Ghost(Monster):
    def __init__(self, level, x, y):
        self.x = x
        self.y = y
        self.tile = Tile.MONSTER_GHOST
        self.dex = int((3 + level) / 1)
        self.str = int((3 + level) / 5)
        self.max_hp = int((3 + level) / 5)
        self.hostility = 3
        self.treasure = level


class Ogre(Monster):
    def __init__(self, level, x, y):
        self.x = x
        self.y = y
        self.tile = Tile.MONSTER_OGRE
        self.dex = int((3 + level) / 5)
        self.str = int((3 + level) * 1.5)
        self.max_hp = int((3 + level) * 1.5)
        self.hostility = 5
        self.treasure = level


class SnakeMage(Monster):
    def __init__(self, level, x, y):
        self.x = x
        self.y = y
        self.tile = Tile.MONSTER_SNAKE_MAGE
        self.dex = int((3 + level) * 1.5)
        self.str = int((3 + level) / 3)
        self.max_hp = int((3 + level) / 3)
        self.hostility = 8
        self.treasure = level


monster_types = [Zombie, Vampire, Ghost, Ogre, SnakeMage]
