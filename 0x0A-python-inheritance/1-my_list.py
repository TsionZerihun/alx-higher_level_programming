#!/usr/bin/python3
"""
File: 1-my_list.py
Desc: This file contains one class; MyList
Author: Tsion
Date Created: 2022
"""


class MyList(list):
    """
    Represents a class MyList
    """

    def print_sorted(self):
        """
        displays the value, but sorted
        (ascending sort)
        """
        print(sorted(self))
