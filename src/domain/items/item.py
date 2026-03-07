ITEM_TYPE_MAPPING = {
    "food": 1,
    "scrolls": 2,
    "elixirs": 3,
    "weapons": 4,
    "treasure": 5
}

class Item:
    def __init__(self, type_name: str, sub_type_name: str):
        self.item_type_code = self._get_item_type(type_name)
        self.item_sub_type = sub_type_name

    def _get_item_type(self, type_name: str):
        item_type_code = ITEM_TYPE_MAPPING.get(type_name)

        if item_type_code is None:
            raise ValueError(f"Unknown item type: {type_name}")

        return item_type_code