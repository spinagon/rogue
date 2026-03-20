from api import DrawTile, Frame, InputEvent, Tile
from .level import Level
from ..entities.character import Character

class Game:
    def __init__(self, ui):
        self.ui = ui
        self.current_depth = 1
        self.level = Level(depth=self.current_depth, player=Character())
        self.descend_next_turn = False

    def loop(self):
        self.ui.draw(self.frame())
        while True:
            if self.level.exited:
                self.advance_depth()
            event = self.ui.get_input()
            if event == InputEvent.QUIT:
                break
            if event is not None:
                self.handle(event)
                self.ui.draw(self.frame())

    def handle(self, event: InputEvent):
        match event:
            case InputEvent.MOVE_UP:
                self.level.move(self.level.player, dy=-1)
                self.level.end_turn()
            case InputEvent.MOVE_DOWN:
                self.level.move(self.level.player, dy=1)
                self.level.end_turn()
            case InputEvent.MOVE_LEFT:
                self.level.move(self.level.player, dx=-1)
                self.level.end_turn()
            case InputEvent.MOVE_RIGHT:
                self.level.move(self.level.player, dx=1)
                self.level.end_turn()
            case InputEvent.USE_WEAPON:
                item_id = self.ui.choose_weapon(
                    [x.display_item() for x in self.level.player.backpack.items]
                )
                if item_id:
                    item = [
                        x for x in self.level.player.backpack.items if id(x) == item_id
                    ]
                    self.level.player.weapon = item
                    self.level.player.backpack.remove(item)
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
        self.level = Level(depth=self.current_depth, player=Character())