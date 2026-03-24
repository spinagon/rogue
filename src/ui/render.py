import curses
from typing import Iterable

from api import DisplayItem, Frame, Tile

TILE_MAP = {
    Tile.EMPTY: " ",
    Tile.WALL_V: "\u2503",
    Tile.WALL_H: "\u2501",
    Tile.CORNER_TL: "\u250f",
    Tile.CORNER_TR: "\u2513",
    Tile.CORNER_BL: "\u2517",
    Tile.CORNER_BR: "\u251b",
    Tile.FLOOR: ".",
    Tile.CHARACTER: "@",
    Tile.CORRIDOR: "#",
    Tile.DOOR: "+",
    Tile.ITEM_WEAPON: "/",
    Tile.ITEM_ELIXIR: "!",
    Tile.ITEM_SCROLL: "%",
    Tile.ITEM_FOOD: "*",
    Tile.ITEM_KEY: "ъ",
    Tile.UNKNOWN: "?",
    Tile.STAIR: ">",
    Tile.MONSTER_ZOMBIE: "z",
    Tile.MONSTER_VAMPIRE: "v",
    Tile.MONSTER_GHOST: "g",
    Tile.MONSTER_OGRE: "o",
    Tile.MONSTER_SNAKE_MAGE: "s",
}

TILE_COLORS = {
    Tile.MONSTER_ZOMBIE: curses.COLOR_GREEN,
    Tile.MONSTER_VAMPIRE: curses.COLOR_RED,
    Tile.MONSTER_OGRE: curses.COLOR_YELLOW,
}


def init(win):
    curses.init_pair(curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # Do not display cursor
    curses.curs_set(False)
    win.leaveok(True)


def draw(win, frame: Frame):
    win.erase()
    for t in frame.tiles:
        char = TILE_MAP.get(t.tile, "?")
        color = TILE_COLORS.get(t.tile, 0)
        win.addstr(t.y, t.x, char, curses.color_pair(color))


def draw_status(win, frame: Frame):
    win.erase()

    win.addstr(f"Level: {frame.level}\n")
    win.addstr(f"HP: {frame.hp}/{frame.max_hp}\n")
    win.addstr(f"Treasure: {frame.treasure}\n")

    win.refresh()


def choose_item(win, items: Iterable[DisplayItem]):
    max_name_length = 20
    top = 5
    left = 20
    width = max_name_length + 10
    height = 9 + 2
    list_box = win.derwin(height, width, top, left)
    list_box.erase()
    list_box.border()
    list_box.addstr(0, 3, "item")
    list_box.addstr(0, max_name_length + 2, "value")
    for i, item in enumerate(items):
        list_box.addstr(i + 1, 1, f"{i + 1:d}")
        list_box.addstr(i + 1, 3, item.name)
        list_box.addstr(i + 1, 3 + max_name_length, f"{item.stat:5d}")
    key = list_box.getkey()
    if "0" <= key <= "9":
        return int(key)
