#!/usr/bin/python3
"""task"""
import sys


def print_status(dicto, file_size):
    """function status """

    print("File size: {}".format(file_size))
    for i, j in sorted(dictio.items()):
        if j != 0:
            print("{}: {}".format(i, j))


file_size = 0
inc = 0
count = 0
dictio = {"200": 0,
          "301": 0,
          "400": 0,
          "401": 0,
          "403": 0,
          "404": 0,
          "405": 0,
          "500": 0}

try:
    for k in sys.stdin:
        k_line = k.split()
        k_line = k_line[::-1]

        if len(k_line) > 2:
            count += 1

            if count <= 10:
                file_size += int(k_line[0])
                inc = k_line[1]

                if (inc in dictio.keys()):
                    dictio[inc] += 1

            if (count == 10):
                print_status(dictio, file_size)
                count = 0

finally:
    print_status(dictio, file_size)
