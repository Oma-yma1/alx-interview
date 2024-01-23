#!/usr/bin/python3
"""task"""
import sys
import signal


def print_stats(total_size, status_codes):
    """function status"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0
total_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 9:
            status_code = tokens[-2]
            file_size = int(tokens[-1])

            total_size += file_size

            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_codes[status_code] = status_codes.get(status_code, 0) + 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    sys.exit(0)
