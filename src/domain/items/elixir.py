from domain.items.item import Item

class Elixir(Item):
    ITEM_TYPE = "elixirs"

    def __init__(self, sub_type_name: str, max_health: int, dexterity: int, strength: int):
        super().__init__(self.ITEM_TYPE, sub_type_name)
        self.max_health = max_health
        self.dexterity = dexterity
        self.strength = strength