import unittest

from src.decisions import Decisions


class Value4(unittest.TestCase):

    def setUp(self):
        self.decisions = Decisions()

    def test_last_digit_4(self):
        self.assertEqual(self.decisions.last_digit_4(14), True)
        self.assertNotEqual(self.decisions.last_digit_4(25), True)
        self.assertEqual(self.decisions.last_digit_4(44), True)
        self.assertEqual(self.decisions.last_digit_4(1854), True)
        self.assertNotEqual(self.decisions.last_digit_4(666), True)
        self.assertTrue(444)

    def test_is_whole_number(self):
        self.assertEqual(self.decisions.is_whole_number(5), True)
        self.assertNotEqual(self.decisions.is_whole_number(5.1), True)
        self.assertTrue(self.decisions.is_whole_number(777))
        self.assertEqual(self.decisions.is_whole_number(999), True)
        self.assertNotEqual(self.decisions.is_whole_number(0.23), True)

    def tearDown(self):
        del(self.decisions)


if __name__ == '__main__':
    unittest.main()
