from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode

class Test(TestCase):
    def test_affine_encode_even_uppercase(self):
        self.assertEqual(affine_encode("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.", 3, 9), "OEV FRHPN MIZXW YZA KRTCL ZUVI OEV QJGD SZB.")
    def test_affine_encode_even_lowercase(self):
        self.assertEqual(affine_encode("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.".lower(), 3, 9), "OEV FRHPN MIZXW YZA KRTCL ZUVI OEV QJGD SZB.")
    def test_affine_encode_even_lower_uppercase(self):
        self.assertEqual(affine_encode("the " + "QUICK BROWN FOX JUMPS OVER THE LAZY DOG.", 3, 9), "OEV FRHPN MIZXW YZA KRTCL ZUVI OEV QJGD SZB.")
    def test_affine_encode_even_3_9(self):
        self.assertEqual(affine_encode("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.", 7, 12), "PJO UWQAE TBGKZ VGR XWSNI GDOB PJO LMFY HGC.")
    def test_affine_encode_one_word_even_empty(self):
        self.assertEqual(affine_encode("", 7, 12), "")
    def test_affine_encode_one_word_even_one_letter(self):
        self.assertEqual(affine_encode("A", 7, 12), "M")
    def test_affine_encode_one_word_even_5_15(self):
        self.assertEqual(affine_encode("A", 5, 15), "P")