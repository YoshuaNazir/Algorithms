import unittest

def whole_number(n): return True if type(n) == int else 0

def negative_number(n): return True if n < 0 else False


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
