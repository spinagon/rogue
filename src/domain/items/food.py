from domain.items.item import Item

class Food(Item):
    ITEM_TYPE = "food"

    def __init__(self, sub_type_name: str, health: int):
        super().__init__(self.ITEM_TYPE, sub_type_name)
        self.health = health
