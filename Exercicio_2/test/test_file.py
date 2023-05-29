import unittest
from WordCounter import WordCounter
from unittest.mock import Mock

class WordCounterTests(unittest.TestCase):

    def test_count_all_words(self):
        observer = Mock()
        counter = WordCounter(observer)
        words = ["Hello", "world", "this", "is", "a", "test"]
        counter.count(words)
        observer.observe.assert_called_with(
            "\nTotal de palavras: 6"
            "\nTotal de palavras com quantidade par de caracteres: 3"
            "\nTotal de palavras começadas com letra maiúscula: 1"
        )

    def test_count_no_words(self):
        observer = Mock()
        counter = WordCounter(observer)
        words = []
        counter.count(words)
        observer.observe.assert_called_with(
            "\nTotal de palavras: 0"
            "\nTotal de palavras com quantidade par de caracteres: 0"
            "\nTotal de palavras começadas com letra maiúscula: 0"
        )

    def test_count_even_char_words(self):
        observer = Mock()
        counter = WordCounter(observer)
        words = ["apple", "banana", "orange", "kiwi"]
        counter.count(words)
        observer.observe.assert_called_with(
            "\nTotal de palavras: 4"
            "\nTotal de palavras com quantidade par de caracteres: 3"
            "\nTotal de palavras começadas com letra maiúscula: 0"
        )

    def test_count_start_uppercase_words(self):
        observer = Mock()
        counter = WordCounter(observer)
        words = ["Audi", "Cupra", "Jaguar", "Mini"]
        counter.count(words)
        observer.observe.assert_called_with(
            "\nTotal de palavras: 4"
            "\nTotal de palavras com quantidade par de caracteres: 3"
            "\nTotal de palavras começadas com letra maiúscula: 4"
        )


if __name__ == "__main__":
    unittest.main()
