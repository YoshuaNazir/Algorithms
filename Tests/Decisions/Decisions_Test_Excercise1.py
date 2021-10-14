import unittest

def iswholenumber(n):
    if type(n) == int:
        return True
    elif type(n) != int:
        raise ValueError("Is not a whole number")

def last_digit_value4(n):
    if n % 10 == 4:
        return True
    elif n % 10 != 4:
        raise ValueError("The last digit is not equals 4")

class DigitValue4(unittest.TestCase):
    def test_last_digit_value4(self):
        self.assertEqual(last_digit_value4(14), True)
        self.assertRaises(ValueError, last_digit_value4, 12)
        self.assertTrue(last_digit_value4(24))

        with self.assertRaises(ValueError):
            last_digit_value4(23)

    def test_iswholenumber(self):
        self.assertEqual(iswholenumber(123), True)
        self.assertTrue(iswholenumber(5))

        with self.assertRaises(ValueError):
            iswholenumber(3.1)



if __name__ == '__main__':
    unittest.main()
