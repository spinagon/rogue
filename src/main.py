import curses
import logging

from game.constants import LEVEL_HEIGHT, LEVEL_WIDTH
from game.game import Game
from ui import render
from ui.input import InputEvent, read_input

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler("debug.log", mode="w"))


def main(stdscr):
    game = Game()
    win = curses.newwin(LEVEL_HEIGHT + 1, LEVEL_WIDTH, 0, 0)
    render.init(win)
    render.draw(win, game.frame())
    while True:
        key = win.getkey()
        event = read_input(key)
        if event == InputEvent.QUIT:
            break
        if event is not None:
            game.handle(event)
            render.draw(win, game.frame())


if __name__ == "__main__":
    curses.wrapper(main)
