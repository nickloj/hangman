# import data
from player import Player
from word import WordManager
from display import DisplayManager


class Game:

    def __init__(self, ui='console'):
        self.player = Player()
        self.word_manager = WordManager()
        self.secret = self.word_manager.get_new_word()

        if ui == 'console':
            self.display_manager = DisplayManager(self)
        else:
            raise ValueError('Not implemented yet')

    def check_guess(self, guess):
        return

    def reveal_letters(self, guessed_letters):
        return ' '.join(letter if letter in guessed_letters
                        else ' _ ' for letter in self.secret)

    def word_guessed(self, guessed_letters):
        return all(letter in guessed_letters for letter in self.secret)

    def play_game(self):
        while (self.player.attempts_left > 0 and
               not self.word_guessed(self.player.guessed_letters)):
            guess = self.player.make_guess()
            self.player.update_attempts(guess in self.secret)
            self.display_manager.show_hangman()
            self.display_manager.show_game_state()
        self.display_manager.show_outcome()
