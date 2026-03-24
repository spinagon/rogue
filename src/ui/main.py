import curses
from typing import Iterable

from api import DisplayItem, Frame
from ui import input, render


class UI:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.win = curses.newwin(self.height + 1, self.width, 0, 0)
        render.init(self.win)

    def get_input(self) -> input.InputEvent | None:
        key = self.win.getkey()
        return input.read_input(key)

    def draw(self, frame: Frame):
        render.draw(self.win, frame)

    def choose_item(self, items: Iterable[DisplayItem]) -> int | None:
        key = render.choose_item(self.win, items)
        if key == 0:
            return 0
        for i, item in enumerate(items):
            if i + 1 == key:
                return item.id
