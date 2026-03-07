from domain.actors.actor import Actor
from domain.actors.backpack import Backpack
from domain.common.position import Position

class Character(Actor):
    def __init__(self, health: int, dexterity: int, strength: int, position: Position):
        super().__init__(health, dexterity, strength, position)
        self.max_health = health
        self.current_weapon = None # Я так понимаю изначально дается какой-то дефолтный меч или что-то типа этого
        self.backpack = Backpack()

    def get_backpack_catalog(self):
        pass