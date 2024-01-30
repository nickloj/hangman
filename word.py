import random
from app.utils import DEFAULT_WORD_LIST


class WordManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(WordManager, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.word_list = set(DEFAULT_WORD_LIST)

    def get_new_word(self) -> str:
        try:
            word = random.choice(list(self.word_list))
            self.word_list.remove(word)
            return word
        except IndexError:
            raise ValueError("No more words in the list.")
