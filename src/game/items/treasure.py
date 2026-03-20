import random
from dataclasses import dataclass

from item import Item

@dataclass
class Treasure(Item):
    @classmethod
    def get_random(cls, level):
        value = random.randint(1, level)
        return cls(value=value)
