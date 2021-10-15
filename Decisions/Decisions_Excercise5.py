# 5. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

def ispair(n):
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        raise ValueError("This number is not pair")
