from utils import HANGMAN_VISUALS
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game


class DisplayManager:
    def __init__(self, game: 'Game'):
        self.game = game
        self.player = game.player
        self.hangman_visuals = HANGMAN_VISUALS

    @staticmethod
    def show_welcome():
        print("""*** Hangman Game *** 
                - You will be presented with a number of missing letters.
                - If you guess correctly, letters will be revealed.
                - Every time you guess a letter wrong you loose a life.
                - Solve the puzzle before the hangman dies.
            """)

    @staticmethod
    def prompt_new_game():
        play = input('Would you like to play again? (y/n):  ')
        if play.lower() != 'y':
            print('Thanks for playing! Goodbye.')
            exit()

    def show_game_state(self):
        word_progress = self.game.reveal_letters(self.player.guessed_letters)
        print("\nWord: ", word_progress)
        print("Attempts left: ", self.player.attempts_left)
        print("Attempted letters: ", ', '.join(self.player.guessed_letters))

    def show_hangman(self):
        print(self.hangman_visuals[self.player.attempts_left])

    def show_outcome(self):
        if self.game.word_guessed(self.player.guessed_letters):
            print("\n 🎉 Congratulations! You've guessed the word!")
        else:
            print("\n 😔 Game Over. The word was:", self.game.secret)
