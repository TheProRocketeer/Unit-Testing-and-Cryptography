from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text

class Test(TestCase):
    def test_convert_to_text_one_word_even_every_letter(self):
        self.assertEqual(convert_to_text(218741750267309021256255930435388550208768849997977, 36), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")
    def test_convert_to_text_one_word_even_empty(self):
        self.assertEqual(convert_to_text(0, 0), "")
    def test_convert_to_text_one_word_odd_A(self):
        self.assertEqual(convert_to_text(0, 1), "A")
    def test_convert_to_text_one_word_even_empty(self):
        self.assertEqual(convert_to_text(0, 4), "AAAA")
    def test_convert_to_text_one_word_even_empty(self):
        self.assertEqual(convert_to_text(11881376, 6), "AAAAAB")
    def test_convert_to_text_one_word_even_empty(self):
        self.assertEqual(convert_to_text(15258, 3), "WOW")