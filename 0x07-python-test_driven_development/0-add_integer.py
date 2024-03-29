#!/usr/bin/python3
"""
No module importation allowed for this task
"""


def add_integer(a, b=98):
    """
        Adds two integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
        
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
