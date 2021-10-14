import unittest

def wholethreedigits(n):
    if n >= 100 and n <= 999:
        return True

    elif n < 100 or n > 999:
        raise ValueError("The number does not have 3 digits")

class MyTestCase(unittest.TestCase):
    def test_wholethreedigit(self):
        self.assertTrue(wholethreedigits(666))
        self.assertEqual(wholethreedigits(101), True)
        self.assertRaises(ValueError, wholethreedigits, 99)
        self.assertRaises(ValueError, wholethreedigits, 1000)







if __name__ == '__main__':
    unittest.main()
