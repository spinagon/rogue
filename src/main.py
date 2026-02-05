from game.game import Game
from ui.input import read_input
from ui.render import draw


def main():
    game = Game()
    while True:
        key = input(">")
        event = read_input(key)
        if event is None:
            break
        game.handle(event)
        draw(game.frame())


if __name__ == "__main__":
    main()
