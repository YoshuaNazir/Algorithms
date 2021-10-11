#1. Leer un número entero y determinar si es un número terminado en 4.

import unittest

def second_digit_value4(n): return n % 10


class Wholenumberseconddigit4(unittest.TestCase):
    def test_seconddigitis4(self):
        self.assertEqual(second_digit_value4(14), 4)  # Is a whole number
        self.assertEqual(second_digit_value4(24), 4)
        self.assertNotEqual(25, 5)  # Should not be equal to 4
        self.assertNotEqual(48, 8)

if __name__ == '__main__':
    unittest.main()
