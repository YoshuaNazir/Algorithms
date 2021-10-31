class Loops:
"""Showing numbers from 1 to the positive number"""
    def show_numbers(self, n):
        for i in range(1, n):
            print(i)

"""Showing pairs from 1 to the introduced number"""
    def show_pairs(n):
        for i in range(1, n):
            if i % 2 == 0:
                print (i)