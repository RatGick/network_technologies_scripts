#!/usr/bin/env python3
# ipgenerator.py - generates IPv4 with the given class
# Usage:
#       py ipgenerator.py ip_class
# ip_class - A, B, C, D, E

import sys
from random import randint, getrandbits

# Take ip_class from command line
ip_class = str(sys.argv[1])

# Create first octet corresponding to the given ip_class
if ip_class == 'A':
    fixed_part = '0'
    remaining_part = bin(getrandbits(7))[2:]
    if len(remaining_part) < 7:  # Because the function could generate any number which bit repr smaller than 8 digits
        remaining_part = (7-len(remaining_part)) * '0' + remaining_part  # Add insufficient zeros in the octet beginning
elif ip_class == 'B':
    fixed_part = '10'
    remaining_part = bin(getrandbits(6))[2:]
    if len(remaining_part) < 6:  # Because the function could generate any number which bit repr smaller than 7 digits
        remaining_part = (6-len(remaining_part)) * '0' + remaining_part  # Add insufficient zeros in the octet beginning
elif ip_class == 'C':
    fixed_part = '110'
    remaining_part = bin(getrandbits(5))[2:]
    if len(remaining_part) < 5:  # Because the function could generate any number which bit repr smaller than 6 digits
        remaining_part = (5-len(remaining_part)) * '0' + remaining_part  # Add insufficient zeros in the octet beginning
elif ip_class == 'D':
    fixed_part = '1110'
    remaining_part = bin(getrandbits(4))[2:]
    if len(remaining_part) < 4:  # Because the function could generate any number which bit repr smaller than 5 digits
        remaining_part = (4-len(remaining_part)) * '0' + remaining_part  # Add insufficient zeros in the octet beginning
elif ip_class == 'E':
    fixed_part = '11110'
    remaining_part = bin(getrandbits(3))[2:]
    if len(remaining_part) < 3:  # Because the function could generate any number which bit repr smaller than 4 digits
        remaining_part = (3-len(remaining_part)) * '0' + remaining_part  # Add insufficient zeros in the octet beginning
else:
    raise ValueError('IP class is not correct')
first_octet = str(int(fixed_part + remaining_part, 2))
ip_address = [first_octet]

# Generate other octets
for i in range(3):
    octet = str(randint(1, 255))
    ip_address.append(octet)

print('.'.join(ip_address))



