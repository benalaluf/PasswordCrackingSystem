import threading
from abc import ABC, abstractmethod
from asyncio import Queue
from concurrent.futures import ProcessPoolExecutor


class GenericDictAttack(ABC):

    def __init__(self, raw_word_list: str, password_hash: str):
        self.raw_word_list = raw_word_list
        self.password_hash = password_hash

        self.word_list = Queue()
        self.__create_word_list()

        self.is_running = True
        self.pool = ProcessPoolExecutor(max_workers=5)
        self.password = None

    def main(self):
        self.__create_word_list()

    @abstractmethod
    def _hash(self, text: str):
        pass

    def __create_word_list(self):
        self.word_list = self.raw_word_list.split('\n')

    def __check_word(self, word: str):
        hashed_word = self._hash(word)
        if hashed_word is self.password_hash:
            self.password = word
            print('found hash', word, hashed_word)
            self.pool.shutdown(wait=False, cancel_futures=True)

    #TODO not finished, research the most efficent way
    def __check_word_list(self):
        while not self.word_list.empty():
            self.pool.submit(self.__check_word, self.word_list.get())


