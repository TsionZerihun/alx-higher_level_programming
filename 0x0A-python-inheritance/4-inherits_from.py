#!/usr/bin/python3
File: 4-inherits_from.py
Desc: This module contains one function;
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited from(directly or indirectly), the specified class;
    otherwise
    False
    """
    return isinstance(obj, a_class) and type(obj) != a_class

def inherits_from(obj, a_class):
    """return True if object is an instance of a class that
    inherited from specified class"""
    if instance(obj, a_class) is True:
        if type(obj) is not a_class:
            return True
    else:
        return False
