from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import substitution_encode

class Test(TestCase):
    def test_substitution_encode_one_word_even(self):
        self.assertEqual(substitution_encode("word", cypher_alpha1), "zrug")