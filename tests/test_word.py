import unittest
from collections import Counter
from app.word import WordManager, DEFAULT_WORD_LIST


WORD_LIST = DEFAULT_WORD_LIST + ['randomdb']


class TestWordManager(unittest.TestCase):
    def setUp(self) -> None:
        self.wm = WordManager(WORD_LIST)
        return super().setUp()

    def test_get_new_word(self):
        word = self.wm.get_new_word()
        self.assertIsInstance(word, str)

    def test_get_new_word_input_list(self):
        word = self.wm.get_new_word()
        self.assertIn(word, WORD_LIST)

    def test_get_new_word_removal(self):
        word = self.wm.get_new_word()
        self.assertNotIn(word, self.wm.word_list)

    def test_get_new_word_randomness(self):
        words = [self.wm.get_new_word() for x in range(len(WORD_LIST))]
        word_counts = Counter(words).values()
        self.assertEqual(max(word_counts), 1)
