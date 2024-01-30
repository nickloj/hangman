import unittest
from unittest.mock import Mock, patch
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.mock_player = Mock()
        self.mock_word_manager = Mock()
        self.mock_word_manager.get_new_word.return_value = 'test'
        self.game = Game(player=self.mock_player,
                         word_manager=self.mock_word_manager)

    def test_init(self):
        self.assertEqual(self.game.player, self.mock_player)
        self.assertEqual(self.game.secret, 'test')

    def test_reveal_letters(self):
        self.secret = 'test'
        self.mock_player.guessed_letters = ['t', 'e']
        self.assertEqual(self.game.reveal_letters(
            self.mock_player.guessed_letters), 't e _ t')

    def test_word_guessed(self):
        self.mock_player.guessed_letters = ['t', 'e', 's']
        self.assertTrue(self.game.word_guessed(
            self.mock_player.guessed_letters))


if __name__ == '__main__':
    unittest.main()
