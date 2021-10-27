class Decisions:

    def last_digit_4(self, n):
        """Determine if the last digit ends in 4"""
        return n % 10 == 4

    def is_whole_number(self, n):
        """Determines if the number is whole"""
        if type(n) == int:
            return True
        else:
            False

    def whole_three_digits(self, n):
        """Determines if the number has three digits """
        if n < 100 or n > 999:
            raise ValueError("Please introduce a 3 digit number")

    def is_negative(self, n):
        """Determines if the number is negative"""
        return n < 0

    def sum_two_digits(self, n):
        if n >= 10 and n <= 99:
            return n // 10 + n % 10

    def two_digit_pair(self, n):
        if n >= 10 and n <= 99:
            return (n // 10) % 2 == 0 and (n % 10) % 2 == 0
