from domain.actors.actor import Actor
from domain.common.position import Position

class Enemy(Actor):
    def __init__(self, health: int, dexterity: int, strength: int, enemy_type: int, hostility: int, position: Position):
        super().__init__(health, dexterity, strength, position)
        self.max_health = health
        self.type = enemy_type
        self.hostility = hostility
