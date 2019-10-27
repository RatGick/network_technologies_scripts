#!/usr/bin/env python3
# ipv6generator.py - generates IPv6
# Usage:
#       py ipv6generator.py

from random import choice
try:
    import pyperclip
except ImportError:
    print('ATTENTION! Please, install pyperclip module by passing \'pip install pyperclip\' into command line to turn on clipboard functionality')

# Create a string with all hex symbols
hex_symbols = '0123456789ABCDEF'
ip_address = []
# Randomly chose 4 digits for 8 parts of the address
for i in range(8):
    ip_part = ''
    for j in range(4):
        digit = choice(hex_symbols)
        ip_part += digit
    ip_address.append(ip_part)

print(':'.join(ip_address))
try:
    pyperclip.copy(':'.join(ip_address))
except NameError:
    pass
