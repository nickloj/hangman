from game import Game
from player import Player
from word import WordManager
from display import DisplayManager as dm


def app():
    dm.show_welcome()
    wm = WordManager()

    while True:
        player = Player()
        game = Game(player=player, word_manager=wm)
        game.play_game()
        dm.prompt_new_game()


if __name__ == "__main__":
    app()
