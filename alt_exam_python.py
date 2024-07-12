"""
BINARY TO DENARY CONVERSION CHALLENGE

You will need to:
- Write a function that takes in a binary string and returns an integer with its converted value.
- Validate binary strings before conversion
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite
"""
import math

class InvalidBinaryStringError(Exception):
    "Custom exception for invalid binary strings."
    pass

def bin2den(binary_string):
    "Converts a binary string to a denary (decimal) integer."
    # Validate the binary string
    if not is_valid_binary(binary_string):
        raise InvalidBinaryStringError(f"Invalid binary string: {binary_string}")

    # Convert binary string to denary value
    denary_value = 0
    binary_string = binary_string[::-1]  # Reverse the string to process from right to left
    for index, digit in enumerate(binary_string):
        if digit == '1':
            denary_value += 2 ** index

    return denary_value

def is_valid_binary(binary_string):
    "Checks if the given string is a valid binary string."
    return all(char in '01' for char in binary_string) and len(binary_string) > 0

#print(bin2den('111111')) Output: 63
#print(bin2den('110021')) Output: InvalidBinaryStringError: Invalid binary string: 110021