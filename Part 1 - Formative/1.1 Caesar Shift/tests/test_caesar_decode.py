from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode

class Test(TestCase):
    def test_caesar_decode_one_word_even_uppercase(self):
        self.assertEqual(caesar_decode("ZRUG", 3), "WORD")
    def test_caesar_decode_one_word_even(self):
        self.assertEqual(caesar_decode("zrug", 3), "word")