from game.api import Frame


def draw(frame: Frame):
    for t in frame.tiles:
        char = t.tile.value
        print(f"draw {char} at {t.y}, {t.x}")
