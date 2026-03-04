import curses

from api import Frame
from ui import input, render


class UI:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.win = curses.newwin(self.height + 1, self.width, 0, 0)
        render.init(self.win)

    def get_input(self) -> input.InputEvent:
        key = self.win.getkey()
        return input.read_input(key)

    def draw(self, frame: Frame):
        render.draw(self.win, frame)
