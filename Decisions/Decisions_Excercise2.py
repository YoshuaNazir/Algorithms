# 2. Leer un número entero y determinar si tiene 3 dígitos.


def count_digit(n):  # This function's purpose is to count the number of digits
    count = 0
    while n != 0:
        n //= 10
        count += 1
        if count == 3:
            print("This is a 3 digit number")
            else var = 0
    return count


def number_is_negative(n):  # This function is to determine wether or not is negative.
    if n < 0:
        return 1
    else:
        0
#Notes: The functions above do not the desired tasks yet and need to be revised, this excercise is still incomplete.