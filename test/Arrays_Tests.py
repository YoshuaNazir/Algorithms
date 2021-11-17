import unittest

from src.arrays import Array



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.arrays = Array()


    def test_max_return_10(self):
        self.assertEqual(self.arrays.Find_max([2, 4, 6, 8, 10]), 10)





if __name__ == '__main__':
    unittest.main()
