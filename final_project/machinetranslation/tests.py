import unittest

from translator import frenchToEnglish, englishToFrench
class TranslationTestCase(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish(''),'')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

    def test_english_to_french(self):
        self.assertEqual(englishToFrench(''),'')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')


if __name__ == '__main__':
    unittest.main()