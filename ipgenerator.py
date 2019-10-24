#!/usr/bin/env python3
# ipgenerator.py - generates IPv4 with the given class
# Don't work
# Usage:
#       ipgenerator.py ip_class
# ip_class - A, B, C, D, E

import sys
import random

# Take ip_class from command line
ip_class = sys.argv[1]
ip_address = []
if ip_class == 'A':
    fixed_part = '0'
    # Because there is already one digit into first octet, get 7-digit number
    changing_part = str(bin(random.getrandbits(7)))[2:]  # Because two first digits - bin header (0b)
    first_octet = str(int(fixed_part + changing_part, 2))  # Convert into decimal
    ip_address.append(first_octet)
elif ip_class == 'B':
    fixed_part = '10'
    # Because there is already two digit into first octet, get 6-digit number
    changing_part = str(bin(random.getrandbits(6)))[2:]  # Because two first digits - bin header (0b)
    first_octet = str(int(fixed_part + changing_part, 2))  # Convert into decimal
    ip_address.append(first_octet)
elif ip_class == 'C':
    fixed_part = '110'
    # Because there is already three digit into first octet, get 5-digit number
    changing_part = str(bin(random.getrandbits(5)))[2:]  # Because two first digits - bin header (0b)
    first_octet = str(int(fixed_part + changing_part, 2))  # Convert into decimal
    ip_address.append(first_octet)
elif ip_class == 'D':
    fixed_part = '1110'
    # Because there is already four digit into first octet, get 4-digit number
    changing_part = str(bin(random.getrandbits(4)))[2:]  # Because two first digits - bin header (0b)
    first_octet = str(int(fixed_part + changing_part, 2))  # Convert into decimal
    ip_address.append(first_octet)
elif ip_class == 'E':
    fixed_part = '11110'
    # Because there is already five digit into first octet, get 3-digit number
    changing_part = str(bin(random.getrandbits(3)))[2:]  # Because two first digits - bin header (0b)
    first_octet = str(int(fixed_part + changing_part, 2))  # Convert into decimal
    ip_address.append(first_octet)
else:
    print('Wrong ip class, please enter A, B, C, D or E')

second_octet = str(bin(random.getrandbits(8)))
second_octet = str(int(second_octet, 2))  # Convert into decimal
ip_address.append(second_octet)

third_octet = str(bin(random.getrandbits(8)))
third_octet = str(int(third_octet, 2))  # Convert into decimal
ip_address.append(third_octet)

fourth_octet = str(bin(random.getrandbits(8)))
fourth_octet = str(int(fourth_octet, 2))  # Convert into decimal
ip_address.append(fourth_octet)

# Print result
print('.'.join(ip_address))




