from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_decode

class Test(TestCase):
    def test_affine_n_decode_even_lowercase(self):
        self.assertEqual(affine_n_decode("oev frhpn mizxw yza krtcl zuvi oev qjgd szb.", 5, 3, 9), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_affine_n_decode_even_uppercase(self):
        self.assertEqual(affine_n_decode("OEV FRHPN MIZXW YZA KRTCL ZUVI OEV QJGD SZB.", 5, 3, 9), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_affine_n_decode_even_upper_lowercase(self):
        self.assertEqual(affine_n_decode("Oev frhpn mizxw yza krtcl zuvi oev qjgd szb.", 5, 3, 9), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_affine_n_decode_even_lowercase(self):
        self.assertEqual(affine_n_decode("oev frhpn mizxw yza krtcl zuvi oev qjgd szb.", 5, 3, 9), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_affine_n_decode_odd_same_number(self):
        self.assertEqual(affine_n_decode("WOZ HBTPD KMXLS EXQ YBNCR XGZM WOZ IFAV UXJ.", 5, 5, 5), "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    def test_affine_n_decode_odd_one_letter(self):
        self.assertEqual(affine_n_decode("P", 5, 5, 15), "A")
    def test_affine_n_decode_one_word_empty(self):
        self.assertEqual(affine_n_decode("", 5, 5, 15), "")
    def test_affine_n_decode_one_word_odd_one(self):
        self.assertEqual(affine_n_decode("M", 5, 7, 12), "A")

#doesnt work