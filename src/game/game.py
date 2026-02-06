from game.api import Tile, InputEvent, DrawTile, Frame
from game import entities


class Game:
    def __init__(self):
        self.player = entities.Character()
        self.level = 1
        self.monsters = [entities.Zombie(self.level, 12, 12)]
        self.items = []

    def handle(self, event: InputEvent):
        match event:
            case InputEvent.MOVE_UP:
                self.player.y -= 1
            case InputEvent.MOVE_DOWN:
                self.player.y += 1
            case InputEvent.MOVE_LEFT:
                self.player.x -= 1
            case InputEvent.MOVE_RIGHT:
                self.player.x += 1

    def frame(self) -> Frame:
        tiles = []
        tiles.extend(
            DrawTile(monster.x, monster.y, monster.tile) for monster in self.monsters
        )
        tiles.append(DrawTile(self.player.x, self.player.y, Tile.CHARACTER))
        return Frame(
            tiles=tiles,
            hp=self.player.hp,
            max_hp=self.player.max_hp,
            treasure=self.player.treasure,
            level=self.level,
        )
