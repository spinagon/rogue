import random
from dataclasses import dataclass
from typing import ClassVar, Tuple

from api import DisplayItem, Tile
from game.base import GameObject


@dataclass
class Item(GameObject):
    hp: int = 0
    max_hp: int = 0
    dex: int = 0
    str_: int = 0
    value: int = 0
    name: str = "Generic item"

    def display_item(self):
        stats: list[Tuple[int, str]] = sorted(
            [
                (self.hp, "hp"),
                (self.max_hp, "max hp"),
                (self.dex, "dex"),
                (self.str_, "str"),
            ]
        )
        max_stat, stat_name = stats[-1]
        return DisplayItem(
            name=self.name,
            stat_name=stat_name,
            stat=max_stat,
            id=id(self),
        )


@dataclass
class Weapon(Item):
    tile: Tile = Tile.ITEM_WEAPON
    names: ClassVar[list[str]] = [
        "mace",
        "sword",
        "dagger",
        "flail",
        "spear",
        "halberd",
    ]

    @classmethod
    def get_random(cls, level):
        value = random.randint(1, level)
        name = random.choice(Weapon.names)
        return cls(str_=value, name=name)


@dataclass
class Treasure(Item):
    @classmethod
    def get_random(cls, level):
        value = random.randint(1, level)
        return cls(value=value)


@dataclass
class Elixir(Item):
    tile: Tile = Tile.ITEM_ELIXIR

    @classmethod
    def get_random(cls, level):
        attr = random.choice(["max_hp", "dex", "str_"])
        value = random.randint(1, level)
        name = ""
        match attr:
            case "max_hp":
                name = "health"
            case "dex":
                name = "dexterity"
            case "str_":
                name = "strength"
            case "_":
                raise Exception(f"No such attribute: {attr}")
        name = f"Elixir of {name}"
        return cls(name=name, **{attr: value})  # type: ignore


@dataclass
class Scroll(Item):
    tile: Tile = Tile.ITEM_SCROLL

    @classmethod
    def get_random(cls, level):
        attr = random.choice(["max_hp", "dex", "str_"])
        value = random.randint(1, level)
        name = ""
        match attr:
            case "max_hp":
                name = "health"
            case "dex":
                name = "dexterity"
            case "str_":
                name = "strength"
            case "_":
                raise Exception(f"No such attribute: {attr}")
        name = f"Scroll of {name}"
        return cls(name=name, **{attr: value})  # type: ignore


@dataclass
class Food(Item):
    names: ClassVar[list[str]] = ["Apple", "Milk", "Bread", "Cheese", "Meat", "Potato"]
    tile: Tile = Tile.ITEM_FOOD

    @classmethod
    def get_random(cls, level):
        value = random.randint(1, level)
        name = random.choice(cls.names)
        return cls(name=name, hp=value)


fist = Weapon(name="No weapon")
