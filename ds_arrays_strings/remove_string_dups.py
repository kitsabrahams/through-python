"""
Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.
"""


def remove_string_duplicate(string):
    current = ''
    for c in sorted(string):
        if c == current:
            string
