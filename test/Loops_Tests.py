import unittest

from src.loops import Loops

class MyTestCase(unittest.TestCase):



    def test_show_pairs(self):
        loops = Loops()
        self.assertListEqual(loops.show_pairs([1, 2, 3, 4, 5, 6]), [2, 4, 6], "Show pairs did not return the expected output")
        self.assertRaises(ValueError, loops.show_pairs, None)



if __name__ == '__main__':
    unittest.main()
