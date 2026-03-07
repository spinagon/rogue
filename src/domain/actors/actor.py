from domain.common.position import Position

class Actor:
    def __init__(self, health: int, dexterity: int, strength: int, position: Position):
        self.health = health
        self.dexterity = dexterity
        self.strength = strength
        self.position = position

    def calculate_damage(self, amount: int):
        pass

    def _take_damage(self, calculated_amount: int):
        pass

    def calculate_attack_damage(self, amount: int):
        pass

    def _get_attack_damage(self, calculated_amount: int):
        pass