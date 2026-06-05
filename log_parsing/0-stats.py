#!/usr/bin/envpython3
"""Log parsing script.

Reads stdin line by line, computes total file size and counts valid status
codes. Prints statistics every 10 lines and on keyboard interruption.
"""

import re
import sys


VALID_STATUS_CODES = (200, 301, 400, 401, 403, 404, 405, 500)

LOG_PATTERN = re.compile(
    r'^(?:\d{1,3}\.){3}\d{1,3} - '
    r'\[[^\]]+\] '
    r'"GET /projects/260 HTTP/1\.1" '
    r'(\S+) (\S+)$'
)


def print_stats(total_size, status_counts):
    """Print the current statistics."""
    print("File size: {}".format(total_size))

    for status_code in VALID_STATUS_CODES:
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))


def parse_line(line):
    """Parse one log line.

    Returns:
        tuple: (status_code, file_size), or None if the line is invalid.
    """
    match = LOG_PATTERN.match(line.strip())

    if match is None:
        return None

    status_code_raw = match.group(1)
    file_size_raw = match.group(2)

    try:
        file_size = int(file_size_raw)
    except ValueError:
        return None

    try:
        status_code = int(status_code_raw)
    except ValueError:
        status_code = None

    return status_code, file_size


def main():
    """Entry point of the script."""
    total_size = 0
    line_count = 0
    status_counts = {code: 0 for code in VALID_STATUS_CODES}

    try:
        for line in sys.stdin:
            line_count += 1

            parsed_line = parse_line(line)

            if parsed_line is not None:
                status_code, file_size = parsed_line

                total_size += file_size

                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
