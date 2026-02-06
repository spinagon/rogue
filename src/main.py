import curses

from game.game import Game
from ui.input import read_input
from ui import render


def main(stdscr):
    curses.curs_set(False)
    game = Game()
    render.init()
    render.draw(stdscr, game.frame())
    while True:
        key = stdscr.getkey()
        event = read_input(key)
        if event is None:
            break
        game.handle(event)
        render.draw(stdscr, game.frame())


if __name__ == "__main__":
    curses.wrapper(main)
