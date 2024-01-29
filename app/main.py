from game import Game
from display import DisplayManager


def app():
    DisplayManager.show_welcome()
    play = 'y'
    while play == 'y':
        game = Game()
        game.play_game()
        play = DisplayManager.new_game()


if __name__ == "__main__":
    app()
