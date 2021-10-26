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
