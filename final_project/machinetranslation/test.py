''' System Testing '''
import unittest
from translator import english_to_french, french_to_english

class Teste2f(unittest.TestCase):
    """ Test en2fr"""
    def test1(self):
        self.assertEqual(english_to_french('0'), '0')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'), '')
        self.assertNotEqual(english_to_french(0), 0)

class Testf2e(unittest.TestCase):
    """ Test fr2en"""
    def test1(self):
        self.assertEqual(french_to_english('0'), '0')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('None'), '')
        self.assertNotEqual(french_to_english(0), 0)

unittest.main()