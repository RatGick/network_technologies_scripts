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
elif ip_class == 'B':
    fixed_part = '10'
elif ip_class == 'C':
    fixed_part = '110'
elif ip_class == 'D':
    fixed_part = '1110'
elif ip_class == 'E':
    fixed_part = '11110'
else:
    raise ValueError('Incorrect IP class. Please, enter either A, B, C, D or E')
# Evaluate the number of digits in the first octet that should be filled
diff = 8 - len(fixed_part)
remaining_part = bin(getrandbits(diff))[2:]  # Generate a digit with the needed length of bin repr, cut off '0b' part
if len(remaining_part) < diff:  # Because the function could generate any number which bin repr smaller than 8 digits
    remaining_part = (diff-len(remaining_part)) * '0' + remaining_part  # Add insufficient zeros in the octet beginning
first_octet = str(int(fixed_part + remaining_part, 2))
ip_address = [first_octet]

# Generate other octets
for i in range(3):
    octet = str(randint(1, 255))
    ip_address.append(octet)

print('.'.join(ip_address))



