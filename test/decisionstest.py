import unittest

from src.decisions import Decisions



class MyTestCase(unittest.TestCase):
    def test_last_digit_4(self):
        self.assertEqual(Decisions.last_digit_4(self, 14), True)


if __name__ == '__main__':
    unittest.main()


