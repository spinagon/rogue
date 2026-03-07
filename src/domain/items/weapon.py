from domain.items.item import Item

class Weapon(Item):
    ITEM_TYPE = "weapons"

    def __init__(self, sub_type_name: str, strength: int):
        super().__init__(self.ITEM_TYPE, sub_type_name)
        self.strength = strength