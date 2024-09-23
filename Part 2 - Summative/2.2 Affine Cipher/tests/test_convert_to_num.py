from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num

class Test(TestCase):
    def test_convert_to_num_one_word_even_empty(self):
        self.assertEqual(convert_to_num("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"), 218741750267309021256255930435388550208768849997977)
    def test_convert_to_num_one_word_even_empty(self):
        self.assertEqual(convert_to_num(""), 0)
    def test_convert_to_num_one_word_even_one_letter(self):
        self.assertEqual(convert_to_num("A"), 0)
    def test_convert_to_num_one_word_odd_uppercase(self):
        self.assertEqual(convert_to_num("ABC"), 1378)
    def test_convert_to_num_one_word_even_multiple_letter(self):
        self.assertEqual(convert_to_num("AAAAAA"), 0)
    def test_convert_to_num_one_word_even_one_letter_lowercase(self):
        self.assertEqual(convert_to_num("a"), 0)
    def test_convert_to_num_one_word_even_lowercase(self):
        self.assertEqual(convert_to_num("abc"), 1378)
    def test_convert_to_num_one_word_even_multiple(self):
        self.assertEqual(convert_to_num("aaaaaaaab"), 208827064576)