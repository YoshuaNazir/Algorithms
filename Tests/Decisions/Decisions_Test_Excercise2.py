import unittest


def count_digit_number(n):
    count: int = 0
    while n != 0:
        n //= 10
        count += 1
    return count

def number_is_negative(n):
    if n < 0:
        return 1
    else:
        0


class MyTestCase(unittest.TestCase):
    def number_is_negative(self):
        self.assertTrue(-1)  # If number is negative needs to be below 0.
        self.assertEqual(12, False)
        self.assertRaises(ValueError, number_is_negative(5))


    def count_digit_number(self):
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
#Notes: The functions above do not complete the desired tasks yet and need to be revised, this excercise is still incomplete.