class Array:

    def Find_max(self, n):
        max = n[0]
        for i in range(0, len(n)):
            if n[i] > max:
                max = n[i]
        return max
