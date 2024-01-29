from game import Game
from display import DisplayManager as dm


def app():
    dm.show_welcome()
    while True:
        game = Game()
        game.play_game()
        dm.prompt_new_game()


if __name__ == "__main__":
    app()
