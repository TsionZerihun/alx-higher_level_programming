#!/usr/bin/python3
"""check if object if instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """return True if object is an instance of a class that
    inherited from specified class"""
    if instance(obj, a_class) is True:
        if type(obj) is not a_class:
            return True
    else:
        return False
