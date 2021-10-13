import unittest

def wholethreedigits(n):
    if n >= 100 and n <= 999: return True

class MyTestCase(unittest.TestCase):
    def test_wholethreedigit(self):
        self.assertTrue(wholethreedigits(666))
        self.assertFalse(wholethreedigits(66))



if __name__ == '__main__':
    unittest.main()
