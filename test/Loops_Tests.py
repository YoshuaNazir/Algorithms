import unittest

from src.loops import Loops

class MyTestCase(unittest.TestCase):

    def setup(self):
        self.loops = Loops()

    def show_numbers(self):
        for i in range(1, 10):
            with self.subTest(self):
                self.assertEqual(i, i)

    def show_pairs(self):
        for i in range(1, 10):
            with self.show_pairs(self):
                self.assertTrue(i % 2, 0)




if __name__ == '__main__':
    unittest.main()
