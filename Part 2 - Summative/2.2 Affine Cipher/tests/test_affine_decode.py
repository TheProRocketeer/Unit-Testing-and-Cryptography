from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode

class Test(TestCase):
    def test_vig_decode_one_word_even_lowercase(self):
        self.assertEqual(affine_decode("oev frhpn mizxw yza krtcl zuvi oev qjgd szb.", 3, 9), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_vig_decode_one_word_even_uppercase(self):
        self.assertEqual(affine_decode("OEV FRHPN MIZXW YZA KRTCL ZUVI OEV QJGD SZB.", 3, 9), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_vig_decode_one_word_even_upper_lowercase(self):
        self.assertEqual(affine_decode("Oev frhpn mizxw yza krtcl zuvi oev qjgd szb.", 3, 9), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_vig_decode_one_word_even_lowercase(self):
        self.assertEqual(affine_decode("oev frhpn mizxw yza krtcl zuvi oev qjgd szb.", 3, 9), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_vig_decode_one_word_odd_same_number(self):
        self.assertEqual(affine_decode("WOZ HBTPD KMXLS EXQ YBNCR XGZM WOZ IFAV UXJ.", 5, 5), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_vig_decode_one_word_odd_one_letter(self):
        self.assertEqual(affine_decode("P", 5, 15), "A")
    def test_vig_decode_one_word_empty(self):
        self.assertEqual(affine_decode("", 5, 15), "")
    def test_vig_decode_one_word_odd_one(self):
        self.assertEqual(affine_decode("M", 7, 12), "A")