from enum import Enum, auto

from api import DrawTile, Frame, InputEvent, Tile
from game.entities.character import Character
from game.game.level import Level
from game.items import Elixir, Food, Scroll, Weapon


class GameStatus(Enum):
    ACTIVE = auto()
    WON = auto()
    LOST = auto()


class Game:
    MAX_DEPTH: int = 21

    def __init__(self, ui):
        self.ui = ui
        self.current_depth = 1
        self.level = Level(depth=self.current_depth, player=Character())
        self.game_status = GameStatus.ACTIVE

    def loop(self):
        self.ui.draw(self.frame())
        while True:
            event = self.ui.get_input()
            if event == InputEvent.QUIT:
                break
            if event is not None:
                self.handle(event)
                self.get_current_game_status()
                self.do_action_by_game_status()
                self.ui.draw(self.frame())

    def get_current_game_status(self):
        if self.level.player.hp <= 0:
            self.game_status = GameStatus.LOST
        elif self.current_depth > Game.MAX_DEPTH:
            self.game_status = GameStatus.WON
        elif self.level.exited:
            self.advance_depth()

    def do_action_by_game_status(self):
        if self.game_status == GameStatus.WON:
            pass
            # TODO present winner screen
        elif self.game_status == GameStatus.LOST:
            pass
            # TODO present loser screen

        # TODO add function to save score in high score table

    def handle(self, event: InputEvent):
        level = self.level
        player = level.player
        backpack = player.backpack
        match event:
            case InputEvent.MOVE_UP:
                level.move(player, dy=-1)
                level.end_turn()
            case InputEvent.MOVE_DOWN:
                level.move(player, dy=1)
                level.end_turn()
            case InputEvent.MOVE_LEFT:
                level.move(player, dx=-1)
                level.end_turn()
            case InputEvent.MOVE_RIGHT:
                level.move(player, dx=1)
                level.end_turn()
            case InputEvent.USE_WEAPON:
                item_id = self.ui.choose_item(
                    [x.display_item() for x in backpack.items if isinstance(x, Weapon)]
                )
                if item_id:
                    item = next(x for x in backpack.items if id(x) == item_id)
                    player.weapon = item
                    backpack.remove(item)
            case InputEvent.USE_FOOD:
                pass
            case InputEvent.USE_ELIXIR:
                pass
            case InputEvent.USE_SCROLL:
                pass

    def in_room(self, room, x: int, y: int) -> bool:
        return room.x0 <= x <= room.x1 and room.y0 <= y <= room.y1

    def draw_rooms(self) -> list[DrawTile]:
        tiles = []
        for room in self.level.rooms:
            for x in range(room.x0, room.x1 + 1):
                tiles.append(DrawTile(x, room.y0, Tile.WALL_H))
                tiles.append(DrawTile(x, room.y1, Tile.WALL_H))
            for y in range(room.y0 + 1, room.y1):
                tiles.append(DrawTile(room.x0, y, Tile.WALL_V))
                tiles.append(DrawTile(room.x1, y, Tile.WALL_V))
            tiles.append(DrawTile(room.x0, room.y0, Tile.CORNER_TL))
            tiles.append(DrawTile(room.x0, room.y1, Tile.CORNER_BL))
            tiles.append(DrawTile(room.x1, room.y0, Tile.CORNER_TR))
            tiles.append(DrawTile(room.x1, room.y1, Tile.CORNER_BR))
            if self.in_room(room, *self.level.player.coords):
                for x in range(room.x0 + 1, room.x1):
                    for y in range(room.y0 + 1, room.y1):
                        tiles.append(DrawTile(x, y, Tile.FLOOR))
        return tiles

    def draw_corridors(self) -> list[DrawTile]:
        tiles = []
        for c in self.level.corridors:
            for x in range(min(c.x0, c.x1), max(c.x0, c.x1) + 1):
                for y in range(min(c.y0, c.y1), max(c.y0, c.y1) + 1):
                    if c.is_inside(x, y):
                        tiles.append(DrawTile(x, y, Tile.CORRIDOR))
        return tiles

    def frame(self) -> Frame:
        tiles = []
        tiles.extend(self.draw_rooms())
        tiles.extend(self.draw_corridors())
        tiles.extend(
            DrawTile(obj.x, obj.y, obj.tile)
            for obj in self.level.monsters + self.level.items
        )
        tiles.append(DrawTile(self.level.player.x, self.level.player.y, Tile.CHARACTER))
        tiles.append(DrawTile(self.level.stair.x, self.level.stair.y, Tile.STAIR))
        ret = Frame(
            tiles=tiles,
            hp=self.level.player.hp,
            max_hp=self.level.player.max_hp,
            treasure=self.level.player.treasure,
            level=self.level.depth,
            message=self.level.message,
        )
        self.level.message = ""
        return ret

    def advance_depth(self):
        self.current_depth += 1
        self.level = Level(depth=self.current_depth, player=self.level.player)
