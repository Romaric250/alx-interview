#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        - data: List of integers representing the data set
    Returns:
        - True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for num in data:
        # Check if the current number is a continuation byte
        if num >> 6 != 0b10:
            # If the current number is not a continuation byte but
            # num_bytes is still greater than 0, it means that the
            # previous character was not properly terminated
            if num_bytes != 0:
                return False

            # Check the number of bytes in the current character
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
        else:
            # If the current number is a continuation byte, it should
            # decrement the number of bytes remaining to complete the
            # current character
            num_bytes -= 1

            # If num_bytes becomes negative, it means that there are
            # more continuation bytes than expected
            if num_bytes < 0:
                return False

    # If there are remaining bytes to complete a character, return False
    if num_bytes != 0:
        return False

    return True
