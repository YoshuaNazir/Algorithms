import unittest

def ispair(n):
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        raise ValueError("This number is not pair")

class MyTestCase(unittest.TestCase):
    def test_ispair(self):
        self.assertEqual(ispair(14), True)
        self.assertEqual(ispair(4), True)
        self.assertEqual(ispair(444), True)
        self.assertTrue(ispair(14))
        self.assertRaises(ValueError, ispair, 15)
        with self.assertRaises(ValueError):
            ispair(333)




if __name__ == '__main__':
    unittest.main()
