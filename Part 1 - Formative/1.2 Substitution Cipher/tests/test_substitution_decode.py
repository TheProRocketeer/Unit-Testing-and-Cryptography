from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import substitution_decode

class Test(TestCase):
    def test_substitution_decode_one_word_even(self):
        self.assertEqual(substitution_decode("zrug", cypher_alpha1), "word")