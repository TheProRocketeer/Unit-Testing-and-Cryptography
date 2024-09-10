from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode
cypher_alpha1 = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
class Test(TestCase):
    def test_substitution_decode_one_word_even(self):
        self.assertEqual(sub_decode("ahou", cypher_alpha1), "word")
    def test_substitution_decode_one_word_even_cap_lower(self):
        self.assertEqual(sub_decode("Ahou", cypher_alpha1), "Word")
    def test_substitution_decode_one_word_even_all_caps(self):
        self.assertEqual(sub_decode("AHOU", cypher_alpha1), "WORD")
    def test_substitution_decode_one_word_odd(self):
        self.assertEqual(sub_decode("ahoun", cypher_alpha1), "words")
    def test_substitution_decode_one_word_odd_cap_lower(self):
        self.assertEqual(sub_decode("Ahoun", cypher_alpha1), "Words")
    def test_substitution_decode_one_word_odd(self):
        self.assertEqual(sub_decode("aha", cypher_alpha1), "wow")
    def test_substitution_decode_one_word_space(self):
        self.assertEqual(sub_decode("w ahou", cypher_alpha1), "a word")