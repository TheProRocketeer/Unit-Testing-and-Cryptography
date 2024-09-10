from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class Test(TestCase):
    def test_caesar_encode_one_word_even_uppercase(self):
        self.assertEqual(caesar_encode("WORD", 3), "ZRUG")

    def test_caesar_encode_one_word_even(self):
        self.assertEqual(caesar_encode("word", 3), "zrug")
    def test_caesar_encode_one_word_even_upper_lower(self):
        self.assertEqual(caesar_encode("Word ", 3), "Zrug ")
    def test_caesar_encode_one_word_even_upper(self):
        self.assertEqual(caesar_encode("WORD", 3), "ZRUG")
    def test_caesar_encode_one_word_odd(self):
        self.assertEqual(caesar_encode("wow", 3), "zrz")
    def test_caesar_encode_one_word_space(self):
        self.assertEqual(caesar_encode("a word", 3), "d zrug")