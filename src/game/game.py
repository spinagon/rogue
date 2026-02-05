from game.api import Tile, InputEvent, DrawTile, Frame


class Game:
    def __init__(self):
        self.player_x = 10
        self.player_y = 10
        self.max_hp = 10
        self.hp = self.max_hp
        self.treasure = 0
        self.level = 1

    def handle(self, event: InputEvent):
        match event:
            case InputEvent.MOVE_UP:
                self.player_y -= 1
            case InputEvent.MOVE_DOWN:
                self.player_y += 1
            case InputEvent.MOVE_LEFT:
                self.player_x -= 1
            case InputEvent.MOVE_RIGHT:
                self.player_x += 1

    def frame(self) -> Frame:
        return Frame(
            tiles=[DrawTile(self.player_x, self.player_y, Tile.CHARACTER)],
            hp=self.hp,
            max_hp=self.max_hp,
            treasure=self.treasure,
            level=self.level,
        )
