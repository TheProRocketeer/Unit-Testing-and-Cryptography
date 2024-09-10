from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode
cypher_alpha1 = "WJKUXVBMIYDTPLHZGONCRSAEFQ"

class Test(TestCase):
    def test_substitution_encode_one_word_even(self):
        self.assertEqual(sub_encode("word", cypher_alpha1), "ahou")
    def test_substitution_encode_one_word_even_Cap_Lower(self):
        self.assertEqual(sub_encode("Word", cypher_alpha1), "Ahou")
    def test_substitution_encode_one_word_even_all_caps(self):
        self.assertEqual(sub_encode("WORD", cypher_alpha1), "AHOU")
    def test_substitution_encode_one_word_odd(self):
        self.assertEqual(sub_encode("words", cypher_alpha1), "ahoun")
    def test_substitution_encode_one_word_odd_caps(self):
        self.assertEqual(sub_encode("WOW", cypher_alpha1), "AHA")
    def test_substitution_encode_one_word_space(self):
        self.assertEqual(sub_encode("a word", cypher_alpha1), "w ahou")