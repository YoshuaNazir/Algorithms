# 3.  Leer un número entero y determinar si es negativo.

def whole_number(n):
    if type(n) == int:
        print("This is a whole number")
    else:
        print("This is not a whole number")


def negative_number(n):
    if n < 0:
        print("This is a negative number")
    else:
        print("This is not a negative number")