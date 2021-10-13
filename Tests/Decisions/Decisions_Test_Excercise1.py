import unittest


def second_digit_value4(n): return 1 if n % 10 == 4 else 0


class DigitValue4(unittest.TestCase):
    def test_last_digit_value4(self):
        self.assertEqual(second_digit_value4(14), True)
        self.assertFalse(second_digit_value4(22), False)


if __name__ == '__main__':
    unittest.main()
