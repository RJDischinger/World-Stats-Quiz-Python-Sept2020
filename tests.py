#tests.py
import unittest

from WorldStatsQuestions import christmas_greeting

class ChristmasTests(unittest.TestCase):
    def test_in_greeting(self):
        self.assertIn("Happy New Year", christmas_greeting(''))

    def test_not_in_greeting(self):
        self.assertNotIn('Easter', christmas_greeting(''))


    def test_empty_string(self):
        with self.assertRaises(ValueError):
            christmas_greeting('')


if __name__ == '__main__':
    unittest.main()
    



