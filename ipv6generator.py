#!/usr/bin/env python3
# ipv6generator.py - generates IPv6
# Usage:
#       py ipv6generator.py

from random import choice
from time import sleep
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

ip_address_short = ip_address.copy()
for i in range(len(ip_address_short)):
    for _ in range(len(ip_address_short[i])-1):
        if ip_address_short[i].startswith('0'):
            ip_address_short[i] = ip_address_short[i][1:]


print(':'.join(ip_address))
print(':'.join(ip_address_short))
try:
    pyperclip.copy(':'.join(ip_address_short))
    sleep(0.01)  # Because CLCL have to be provided with some time window
    pyperclip.copy(':'.join(ip_address))
except NameError:
    pass
