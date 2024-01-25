#!/usr/bin/python3
"""Reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (lines not in this format are skipped)

After every 10 lines or a keyboard interruption (CTRL + C),
print the following statistics:
- Total file size: <total size> (sum of all previous file sizes)
- Number of lines by status code (status codes in ascending order)

Status codes: 200, 301, 400, 401, 403, 404, 405, 500
Status codes that don't appear or are not integers are not printed.
"""

import sys

# Store the count of all status codes in a dictionary
status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                      '404': 0, '405': 0, '500': 0}

total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in status_code_counts.keys():
                status_code_counts[status_code] += 1

            total_file_size += file_size

            line_count += 1

        if line_count == 10:
            line_count = 0  # Reset line count
            print('Total file size: {}'.format(total_file_size))

            for key, value in sorted(status_code_counts.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('Total file size: {}'.format(total_file_size))
    for key, value in sorted(status_code_counts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
