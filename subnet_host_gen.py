#!/usr/bin/env python3
# subnet_host_gen.py - generates a subnet mask with the given number of subnets and hosts
# Usage:
#       py host_subnet_get.py subnets hosts
# subnets - number of subnets in the generated mask
# hosts - number of hosts in the generated mask

import sys
import math

# Grab variables from command line
subnets = int(sys.argv[1])
hosts = int(sys.argv[2])

# Calculate the number of zeros and ones in the mask
zeros_number = int(math.ceil(math.log2(hosts+2)))
ones_number = int(math.ceil(math.log2(subnets)))

# Generate mask
if zeros_number + ones_number < 32:
    remaining_number = 32 - zeros_number - ones_number
    mask_bits = remaining_number + ones_number  # mask in bits representation (192.1.168.3/20)
    mask_bin = '1' * mask_bits + '0' * zeros_number  # mask in binary representation
    assert len(mask_bin) == 32  # mask length must consist of 32 digits
    # Convert mask into decimal and create bin representation separated with dots
    mask = []
    mask_bin_with_dots = []
    for i in range(0, 32, 8):
        octet = mask_bin[i:i + 8]
        mask_bin_with_dots.append(octet)
        octet = str(int(octet, 2))
        mask.append(octet)

    mask_bin_with_dots = '.'.join(mask_bin_with_dots)
    mask = '.'.join(mask)

    # Count exact number of subnets and hosts in the resulting mask
    mult_8_list = [8, 16, 24, 32]  # list of all multiplications on 8
    for i in range(len(mult_8_list)):
        # Find the last mult_8 smaller than mask bits
        if mult_8_list[i] > mask_bits:
            subnets_result = mask_bits - mult_8_list[i-1]
            subnets_result = 2 ** subnets_result
            break  # leave the loop because the value have been already found

    hosts_result = mask_bin_with_dots.count('0')
    hosts_result = 2 ** hosts_result - 2

    print(f'Mask decimal: {mask}, mask bits: {mask_bits}, mask binary: {mask_bin_with_dots}')
    print(f'Number of subnets: {subnets_result}, number of hosts: {hosts_result}')
else:
    print('Mask with the given parameters does not exist')
