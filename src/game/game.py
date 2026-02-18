import random
from typing import cast

from game import entities, items, rooms
from game.api import DrawTile, Frame, InputEvent, Tile


class Level:
    def __init__(self, depth: int, player: entities.Character):
        self.player = player
        self.depth = depth
        self.rooms: list[rooms.Room] = [rooms.Room(i) for i in range(9)]
        self.corridors = [rooms.Corridor(self.rooms[:2])]
        self.starting_room: int = random.randint(0, 8)
        x = (self.rooms[self.starting_room].x0 + self.rooms[self.starting_room].x1) // 2
        y = (self.rooms[self.starting_room].y0 + self.rooms[self.starting_room].y1) // 2
        self.place(player, x, y)
        self.items: list[items.Item] = self.place_items()
        self.monsters: list[entities.Monster] = self.place_monsters()

    def place(self, obj: entities.GameObject, x=None, y=None):
        obj.place(x, y)

    def move(self, obj: entities.GameObject, dx=0, dy=0):
        target = self[obj.x + dx, obj.y + dy]
        if target in [Tile.FLOOR, Tile.CORRIDOR]:
            obj.move(dx, dy)
        if isinstance(target, items.Item):
            self.remove(target)
            self.player.backpack.items.append(target)

    def remove(self, obj: entities.GameObject):
        match type(obj):
            case entities.Monster:
                self.monsters.remove(cast(entities.Monster, obj))
            case items.Item:
                self.items.remove(cast(items.Item, obj))

    def place_monsters(self) -> list[entities.Monster]:
        monsters = []
        n_monsters = self.depth + 2
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
            monsters.append(monster_type(depth=self.depth, x=x, y=y))
        return monsters

    def place_items(self) -> list[items.Item]:
        new_items = []
        n_items = self.depth + 2
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
            new_items.append(item_type.get_random(level=self.depth))
            self.place(new_items[-1], x=x, y=y)
        return new_items

    def __getitem__(self, k):
        x, y = k
        for c in self.corridors:
            if c.is_inside(x, y):
                return Tile.CORRIDOR
        for room in self.rooms:
            if room.is_wall(x, y):
                return Tile.WALL_H
            if room.is_floor(x, y):
                for item in self.items:
                    if (item.x, item.y) == (x, y):
                        return item
                for m in self.monsters:
                    if (m.x, m.y) == (x, y):
                        return m
                return Tile.FLOOR
        return Tile.EMPTY


class Game:
    def __init__(self):
        self.level = Level(depth=1, player=entities.Character())

    def handle(self, event: InputEvent):
        match event:
            case InputEvent.MOVE_UP:
                self.level.move(self.level.player, dy=-1)
            case InputEvent.MOVE_DOWN:
                self.level.move(self.level.player, dy=1)
            case InputEvent.MOVE_LEFT:
                self.level.move(self.level.player, dx=-1)
            case InputEvent.MOVE_RIGHT:
                self.level.move(self.level.player, dx=1)

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
        return Frame(
            tiles=tiles,
            hp=self.level.player.hp,
            max_hp=self.level.player.max_hp,
            treasure=self.level.player.treasure,
            level=self.level.depth,
            message=f"{self.level.player.x=} {self.level.player.y=}",
        )
