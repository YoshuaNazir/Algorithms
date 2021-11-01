class Loops:

    # Showing numbers from 1 to the positive number
    def show_numbers(self, n):
        for i in range(1, n):
            print(i)

    # Showing pairs from 1 to the introduced number
    def show_pairs(self, n):
        for i in range(1, n):
            if i % 2 == 0:
                print(i)

    # Showing exact dividers of the introduced numbers
    def show_dividers(n):
        for i in range(1, n):
            if n % i == 0:
                print(i)


    def show_whole_numbers(self,n1,n2):
        if n1 < n2:
            First = n1
            Second = n2
        if n2 < n1:
            First = n2
            Second = n1
        for i in range(First, Second):
            if i > 0:
            print(i)