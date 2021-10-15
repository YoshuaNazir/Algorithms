import unittest

def sumtwodigit(n):
    if n >= 10 and n <= 99:
        return n // 10 + n % 10
    elif n < 10 or n > 99:
        raise ValueError("This is not a two digit number")

class MyTestCase(unittest.TestCase):
    def test_sumtwodigit(self):
        self.assertEqual(sumtwodigit(88), 16)
        self.assertEqual(sumtwodigit(66), 12)
        self.assertNotEqual(sumtwodigit(13), 5)
        self.assertRaises(ValueError, sumtwodigit, 100)
        with self.assertRaises(ValueError):
            sumtwodigit(8)



if __name__ == '__main__':
    unittest.main()
