from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text

class Test(TestCase):
    def test_affine_encode_one_word_even_empty(self):
        self.assertEqual(convert_to_text(num, n), "")