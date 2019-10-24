#!/usr/bin/env python3
# ip_and_mask_get.py - generates IPv4 with the given class

import random

# Generate random IP
ip_address = []

for i in range(4):
    octet = random.randint(1, 255)
    ip_address.append(octet)

# Generate random mask
mask = []

first_octet = random.randint(1, 255)
if first_octet == 255:
    second_octet = random.randint(1, 255)
    if second_octet == 255:
        third_octet = random.randint(1, 255)
        if third_octet == 255:
            fourth_octet = random.randint(1, 254)
        else:
            fourth_octet = 0
    else:
        third_octet = 0
        fourth_octet = 0
else:
    second_octet = 0
    third_octet = 0
    fourth_octet = 0

mask.append(first_octet)
mask.append(second_octet)
mask.append(third_octet)
mask.append(fourth_octet)

# Generate network IP
i = 0
network = []
for ip_octet in ip_address:
    network_octet = ip_octet & mask[i]
    network.append(network_octet)
    i += 1

for i in range(len(ip_address)):
    ip_address[i] = str(ip_address[i])
    mask[i] = str(mask[i])
    network[i] = str(network[i])

print(f"IPv4: {'.'.join(ip_address)}, mask: {'.'.join(mask)}, network: {'.'.join(network)}")