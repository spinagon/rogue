import curses

from game.api import Frame, Tile

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
    Tile.ITEM_WEAPON: "/",
    Tile.ITEM_ELIXIR: "!",
    Tile.ITEM_SCROLL: "%",
    Tile.ITEM_FOOD: "*",
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


def init():
    curses.init_pair(curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)


def draw(stdscr, frame: Frame):
    stdscr.erase()
    for t in frame.tiles:
        char = TILE_MAP.get(t.tile, "?")
        color = TILE_COLORS.get(t.tile, 0)
        stdscr.addstr(t.y, t.x, char, curses.color_pair(color))

    # Draw status bar
    height, width = stdscr.getmaxyx()
    status = f"Level: {frame.level} | HP: {frame.hp}/{frame.max_hp} | Treasure: {frame.treasure}"
    stdscr.addstr(height - 1, 0, status[:width])

    stdscr.refresh()
