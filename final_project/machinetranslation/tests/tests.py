"this file purpose is for testing translator.py"
import unittest
import translator

class Test_englishToFrench(unittest.TestCase):
    "test englishToFrench"
    def testenglishtofrench(self):
        "it will be equal "
        self.assertEqual(translator.englishToFrench("Hello"),"Bonjour")

class Test_frenchToEnglish(unittest.TestCase):
    "test frenchToEnglish"
    def testfrenchtoenglish(self):
        "it will be equal "
        self.assertEqual(translator.frenchToEnglish("Bonjour"),"Hello")

unittest.main()
