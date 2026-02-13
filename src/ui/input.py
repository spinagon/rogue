from game.api import InputEvent

KEYMAP = {
    "w": InputEvent.MOVE_UP,
    "a": InputEvent.MOVE_LEFT,
    "s": InputEvent.MOVE_DOWN,
    "d": InputEvent.MOVE_RIGHT,
    "q": InputEvent.QUIT,
}


def read_input(key: str) -> InputEvent | None:
    return KEYMAP.get(key)
