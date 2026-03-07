from domain.items.item import Item

class Weapon(Item):
    ITEM_TYPE = "treasure"

    def __init__(self, sub_type_name: str, value: int):
        super().__init__(self.ITEM_TYPE, sub_type_name)
        self.value = value