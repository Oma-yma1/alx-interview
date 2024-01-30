#!/usr/bin/python3
"""
file
"""


def validUTF8(data):
    """utf8 validation"""
    num_byte = 0
    for by in data:
        if num_byte == 0:
            coun = 1 << 7
            while coun & by:
                num_byte += 1
                coun >>= 1
            if num_byte == 0:
                continue
            if num_byte == 1 or num_byte > 4:
                return False
        else:
            if not (by & (1 << 7) and not (by & (1 << 6))):
                return False
        num_byte -= 1
    return num_byte == 0
