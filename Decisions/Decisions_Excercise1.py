#1. Leer un número entero y determinar si es un número terminado en 4.

def last_digit_value4(n):
    if n % 10 == 4:
        print("Second digit equals 4")
    else:
        raise ValueError("The last digit is not equals 4")

def iswholenumber(n):
    if type(n) == int:
        return True
    elif type(n) != int:
        raise ValueError("Is not a whole number")