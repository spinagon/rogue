import random

from game.api import Tile, InputEvent, DrawTile, Frame
from game import entities, items, rooms


class Game:
    def __init__(self):
        self.player = entities.Character()
        self.level = 1
        self.rooms = [rooms.Room(i) for i in range(9)]
        self.starting_room = random.randint(0, 8)
        self.player.x = (
            self.rooms[self.starting_room].x0 + self.rooms[self.starting_room].x1
        ) // 2
        self.player.y = (
            self.rooms[self.starting_room].y0 + self.rooms[self.starting_room].y1
        ) // 2
        self.monsters = self.place_monsters()
        self.items = self.place_items()

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
        for room in self.rooms:
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
            for x in range(room.x0 + 1, room.x1):
                for y in range(room.y0 + 1, room.y1):
                    tiles.append(DrawTile(x, y, Tile.FLOOR))
        tiles.extend(
            DrawTile(obj.x, obj.y, obj.tile) for obj in self.monsters + self.items
        )
        tiles.append(DrawTile(self.player.x, self.player.y, Tile.CHARACTER))
        return Frame(
            tiles=tiles,
            hp=self.player.hp,
            max_hp=self.player.max_hp,
            treasure=0,
            level=self.level,
        )

    def place_monsters(self):
        monsters = []
        n_monsters = self.level + 2
        to_place = random.choices(
            entities.monster_types, k=n_monsters, weights=[0.5, 0.3, 0.2, 0.1, 0.1]
        )
        for monster_type in to_place:
            room_id = random.randint(0, 8)
            if room_id == self.starting_room:
                room_id = (room_id + 1) % 9
            room = self.rooms[room_id]
            x = random.randint(room.x0 + 1, room.x1 - 1)
            y = random.randint(room.y0 + 1, room.y1 - 1)
            monsters.append(monster_type(level=self.level, x=x, y=y))
        return monsters

    def place_items(self):
        new_items = []
        n_items = self.level + 2
        to_place = random.choices(
            [
                items.Weapon,
                items.Elixir,
                items.Scroll,
                items.Food,
            ],
            k=n_items,
            weights=[0.1, 0.2, 0.2, 0.5],
        )
        for item_type in to_place:
            room_id = random.randint(0, 8)
            if room_id == self.starting_room:
                room_id = (room_id + 1) % 9
            room = self.rooms[room_id]
            x = random.randint(room.x0 + 1, room.x1 - 1)
            y = random.randint(room.y0 + 1, room.y1 - 1)
            new_items.append(item_type.get_random(level=self.level))
            new_items[-1].x = x
            new_items[-1].y = y
        return new_items
