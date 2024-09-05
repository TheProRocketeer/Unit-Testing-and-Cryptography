from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class Test(TestCase):
    def test_caesar_encode_one_word_even(self):
        self.assertEqual(caesar_encode("word", 3), "zrug")