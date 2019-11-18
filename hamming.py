#!/usr/bin/env python3
# hamming — generates bits with the hamming encoding
# Usage:
#       py hamming.py -number N
# N — number of bits in an encoded sequence, default — random from 11 to 20

import random
import argparse
import math


def get_print_form(list: list) -> str:
    for index in range(len(list)):
        list[index] = str(list[index])
    return ''.join(list)


parser = argparse.ArgumentParser(description='Generates bits with the hamming encoding')
parser.add_argument('-number', type=int, default=-1, help='Number of bits in an encoded sequence, default — random from 11 to 20.')
args = parser.parse_args()

if args.number <= 0:  # to prevent from a negative input
    N = random.randint(11, 20)
else:
    N = args.number

bits = [random.randint(0, 1) for _ in range(N)]

# Find positions for parity bits and insert placeholders there
positions = [2 ** x - 1 for x in range(math.ceil(math.log2(N)))]  # positions — powers of 2 minus 1 (indexes start from 0)
for index in range(len(positions)):
    bits.insert(positions[index], 'placeholder')

# Get bits required to calculate the parity bits
calculation_dict = {str(position): [] for position in positions}
keys = list(calculation_dict.keys())
for position_index in range(1, len(positions) + 1):
    for bit_index in range(1, len(bits) + 1):
        if isinstance(bits[bit_index-1], str):
            continue
        if len(bin(bit_index)) >= (position_index + 2) and bin(bit_index)[-position_index] == '1':
            calculation_dict[keys[position_index - 1]].append(bits[bit_index - 1])

# Calculate parity bits and append them
parity_bits = []
for key in keys:
    parity_itter = calculation_dict[key][0]
    for index in range(1, len(calculation_dict[key])):
        parity_itter = parity_itter ^ calculation_dict[key][index]
    parity_bits.append(parity_itter)

for index in range(len(positions)):
    del bits[positions[index]]
    bits.insert(positions[index], parity_bits[index])

print(f"Code: {get_print_form(bits)}, parity bits: {get_print_form(parity_bits)}")
