import unittest



def iswholenumber(n):
    if type(n) == int:
        return True
    elif type(n) != int:
        raise ValueError("This is not a whole number")


def isnegative(n):
    if n < 0:
        return True
    elif n >= 0:
        raise ValueError("Please insert a negative number")


class MyTestCase(unittest.TestCase):
    def test_isnegative(self):
        self.assertEqual(isnegative(-5), True)
        self.assertTrue(isnegative(-69))
        self.assertRaises(ValueError, isnegative, 0)

        with self.assertRaises(ValueError):
            isnegative(78)


if __name__ == '__main__':
    unittest.main()
