from dataclasses import dataclass
import random


@dataclass
class Item:
    hp: int = 0
    max_hp: int = 0
    dex: int = 0
    str: int = 0
    value: int = 0
    name: str = "Generic item"


class Weapon(Item):
    names: list[str] = ["mace", "sword", "dagger", "flail", "spear", "halberd"]

    @classmethod
    def get_random(self, level):
        value = random.randint(1, level)
        self.str = value
        self.name = random.choice(self.names)


class Treasure(Item):
    @classmethod
    def get_random(self, level):
        value = random.randint(1, level)
        self.value = value


class Elixir(Item):
    @classmethod
    def get_random(self, level):
        attr = random.choice(["max_hp", "dex", "str"])
        value = random.randint(1, level)
        setattr(self, attr, value)
        match attr:
            case "max_hp":
                name = "health"
            case "dex":
                name = "dexterity"
            case "str":
                name = "strength"
            case "_":
                raise Exception(f"No such attribute: {attr}")
        self.name = f"Elixir of {name}"


class Scroll(Item):
    @classmethod
    def get_random(self, level):
        attr = random.choice(["max_hp", "dex", "str"])
        value = random.randint(1, level)
        setattr(self, attr, value)
        match attr:
            case "max_hp":
                name = "health"
            case "dex":
                name = "dexterity"
            case "str":
                name = "strength"
            case "_":
                raise Exception(f"No such attribute: {attr}")
        self.name = f"Scroll of {name}"


class Food(Item):
    names: list[str] = ["Apple", "Milk", "Bread", "Cheese", "Meat", "Potato"]

    @classmethod
    def get_random(self, level):
        value = random.randint(1, level)
        self.hp = value
        self.name = random.choice(self.names)


fist = Weapon(name="No weapon")
