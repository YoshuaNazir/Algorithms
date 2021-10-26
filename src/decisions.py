class Decisions:

    def last_digit_4(self, n):
        """Determine if the last digit ends in 4"""
        return n % 10 == 4

    def is_whole_number(self, n):
        if type(n) == int:
            return True
        else:
            False