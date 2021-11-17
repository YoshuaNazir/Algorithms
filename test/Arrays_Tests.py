import unittest

from src.arrays import Array



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.arrays = Array()
        self.input = [2, 4, 6, 8, 10]
        self.output = 10

    def test_max(self):
        self.assertEqual(self.arrays.Find_max(self.input, self.output))





if __name__ == '__main__':
    unittest.main()
