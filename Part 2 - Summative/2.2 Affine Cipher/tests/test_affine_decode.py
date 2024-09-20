from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode

class Test(TestCase):
    def test_vig_decode_one_word_even_uppercase(self):
        self.assertEqual(affine_decode("Oev frhpn mizxw yza krtcl zuvi oev qjgd szb.", 3, 9), "The quick brown fox jumps over the lazy dog.")