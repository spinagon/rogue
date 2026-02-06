import curses

from game.api import Frame, Tile

override_colors = {
    Tile.MONSTER_ZOMBIE: curses.COLOR_GREEN,
    Tile.MONSTER_VAMPIRE: curses.COLOR_RED,
    Tile.MONSTER_OGRE: curses.COLOR_YELLOW,
}


def init():
    curses.init_pair(curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)


def draw(stdscr, frame: Frame):
    stdscr.clear()
    for t in frame.tiles:
        char = t.tile.value
        color = override_colors.get(t.tile, 0)
        stdscr.addstr(t.y, t.x, char, curses.color_pair(color))
    stdscr.refresh()
