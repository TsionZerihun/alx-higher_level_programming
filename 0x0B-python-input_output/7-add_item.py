#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then save them to a file
"""


import sys
import os.path
import json
#save = __import__('5-save_to_json_file').save_to_json_file
def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
    using a JSON representation """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
#load = __import__('6-load_from_json_file').load_from_json_file
def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file” """
    with open(filename, 'r') as f:
        return (json.load(f))

filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])

save_to_json_file(json_list, filename)
