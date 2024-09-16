from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class Test(TestCase):
    def test_vig_decode_one_word_even_uppercase(self):
        self.assertEqual(vig_decode("OSS ", "TEST"), "WOAH")
    def test_vig_decode_one_word_even_lower_key(self):
        self.assertEqual(vig_decode("OSS ", "test"), "WOAH")
    def test_vig_decode_one_word_even_lower_text(self):
        self.assertEqual(vig_decode("oss ", "test"), "WOAH")
    def test_vig_decode_one_word_even_spaces(self):
        self.assertEqual(vig_decode("OSNSDSFC", "TEST"), "WOW LOOK")
    def test_vig_decode_one_word_even_spaces_lower_key(self):
        self.assertEqual(vig_decode("OSNSDSFC", "TEST"), "WOW LOOK")
    def test_vig_decode_one_word_even_spaces_lower_key(self):
        self.assertEqual(vig_decode("OSNSDSFC", "test"), "WOW LOOK")
    def test_vig_decode_one_word_odd_spaces_lower_key(self):
        self.assertEqual(vig_decode("OSS SPFGC", "test"), "WOAH LOOK")