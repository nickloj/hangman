import random


DEFAULT_WORD_LIST = ["mysql", 'postgresql', "redis", "mongodb", "sqlite",
                     "oracle", "cassandra", "mariadb", "mssql", "sybase",
                     "teradata", "informix", "access", "elastic", "couchdb",
                     "couchbase",  "hbase", "ravendb", "firebase", "dynamodb",]


class WordManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WordManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, word_list: list = DEFAULT_WORD_LIST) -> None:
        print(f"Initializing with args: {word_list},")
        self.word_list = set(word_list)

    def get_new_word(self) -> str:
        try:
            word = random.choice(list(self.word_list))
            self.word_list.remove(word)
            return word
        except IndexError:
            raise ValueError("No more words in the list.")
