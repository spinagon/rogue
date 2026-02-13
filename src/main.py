import curses

from game.game import Game
from ui.input import read_input, InputEvent
from ui import render


def main(stdscr):
    game = Game()
    render.init(stdscr)
    render.draw(stdscr, game.frame())
    while True:
        key = stdscr.getkey()
        event = read_input(key)
        if event == InputEvent.QUIT:
            break
        if event is not None:
            game.handle(event)
            render.draw(stdscr, game.frame())


if __name__ == "__main__":
    curses.wrapper(main)
