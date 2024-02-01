#!/usr/bin/python3
"""
UTF-8 Validation script
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        - data: List of integers representing the data set
    Returns:
        - True if data is a valid UTF-8 encoding, else False
    """

    num_bytes = 0

    for num in data:
        # Check if the current number is a continuation byte
        if num >> 6 == 0b10:
            # previous character was not properly terminated
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            # Check the number of bytes in the current character
            if num_bytes != 0:
                return False

            # Get the number of bytes in the current UTF-8 character
            if num >> 7 == 0b0:
                num_bytes = 0
            elif num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False

    # If there are remaining bytes to complete a character, return False
    if num_bytes != 0:
        return False

    return True
