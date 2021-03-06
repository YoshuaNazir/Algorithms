class Loops:

    # Showing numbers from 1 to the positive number
    def show_numbers(self, n):
        for i in range(1, n):
            print(i)

    # Showing pairs from 1 to the introduced number
    def show_pairs(self, n):
        if type(n) is not list:
            raise ValueError("Not a list")
        pairs = []
        for i in n:
            if i % 2 == 0:
                pairs.append(i)
        return pairs

    # Showing exact dividers of the introduced numbers
    def show_dividers(n):
        for i in range(1, n):
            if n % i == 0:
                print(i)

    # Showing the whole numbers between the introduced number
    def show_whole_numbers(self,n1,n2):
        first = n1 if n1 < n2 else n2
        second = n2 if n2 > n1 else n1

        for i in range(first, second):
            if i > 0:
                print(i)

      #Shows all the numbers from the range that ends in 4
    def Show_range_ends_4(self, n1, n2):
        if n1 < n2:
            First = n1
            Second = n2
        if n2 < n1:
            First = n2
            Second = n1
        for i in range(First,Second):
            if i % 10 == 4:
                print(i)