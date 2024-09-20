from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class Test(TestCase):
    def test_vig_encode_one_word_even_uppercase(self):
        self.assertEqual(vig_encode("WOAH", "TEST"), "OSS ")
    def test_vig_encode_one_word_even_lower_key(self):
        self.assertEqual(vig_encode("WOAH", "test"), "OSS ")
    def test_vig_encode_one_word_even_uppercase_spaces(self):
        self.assertEqual(vig_encode("WOW LOOK", "TEST"), "OSNSDSFC")
    def test_vig_encode_one_word_even_spaces_lower_key(self):
        self.assertEqual(vig_encode("WOW LOOK", "test"), "OSNSDSFC")
    def test_vig_encode_one_word_odd_space(self):
        self.assertEqual(vig_encode("WOAH LOOK", "TEST"), "OSS SPFGC")
    def test_vig_encode_one_word_odd_space_lower_key(self):
        self.assertEqual(vig_encode("WOAH LOOK", "test"), "OSS SPFGC")