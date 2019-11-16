#!/usr/bin/env python3
# crc_gen — generates a sequence of bits with CRC remainder and the corresponding CRC polynom (divisor)

import numpy as np
import random


def get_print_form(array) -> str:
    array = array.astype('int')
    array = list(array.astype(str))
    str_to_print = ''.join(array)
    return str_to_print


while True:
    # Generate a random polynom
    power_polynom = random.randint(3, 10)
    polynom = [random.randint(0, 1) for _ in range(power_polynom)]
    polynom[0] = 1  # First bit is always has to be 1, otherwise its power automatically decreases
    polynom = np.array(polynom)
    # Generate a random divisor with a smaller power
    power_divisor = power_polynom - random.randint(1, power_polynom-2)
    divisor = [random.randint(0, 1) for _ in range(power_divisor)]
    divisor[0] = 1  # First bit is always has to be 1, otherwise its power automatically decreases
    divisor = np.array(divisor)

    remainder = np.polydiv(polynom, divisor)[1]

    polynom_with_remainder = np.append(polynom, remainder)

    check = np.polydiv(polynom_with_remainder, divisor)[1]
    if not np.any(polynom_with_remainder > 1) and not np.any(polynom_with_remainder < 0):  # The array should only contain 1 and 0
        if len(check) == 1 and check == 0:
            break

print(f'Original bits: {get_print_form(polynom)}, remainder: {get_print_form(remainder)}')
print(f'CRC polynom: {get_print_form(divisor)}, bits with CRC: {get_print_form(polynom_with_remainder)}')
