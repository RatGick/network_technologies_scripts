#!/usr/bin/env python3
# ip_and_mask_get.py - generates IPv4 with the given class

from random import randint

# Generate random IP
ip_address = []

for i in range(4):
    octet = randint(1, 255)
    ip_address.append(octet)

# Generate random mask in number format (192.168.1.3/25)
mask_number = randint(1, 31)
# Create mask in binary representation
mask_bin_ones = '1' * mask_number
mask_bin_zeros = '0' * (32 - mask_number)
mask_bin = mask_bin_ones + mask_bin_zeros
# Split it into octets:
mask = []
for i in range(0, 32, 8):
    octet = mask_bin[i:i+8]
    octet = int(octet, 2)
    mask.append(octet)

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