# 2. Leer un número entero y determinar si tiene 3 dígitos.

def wholethreedigits(n):
    if n >= 100 and n <= 999:
        return True

    elif n < 100 or n > 999:
        raise ValueError("The number does not have 3 digits")
