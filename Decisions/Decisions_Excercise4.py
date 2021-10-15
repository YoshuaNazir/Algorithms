# 4. Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus dígitos.

def sumtwodigit(n):
    if n >= 10 and n <= 99:
        return n // 10 + n % 10
    elif n < 10 or n > 99:
        raise ValueError("This is not a two digit number")
