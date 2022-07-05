#!/usr/bin/python3
""" Function """
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    js_list = load_from_json_file("add_item.json")
except Exception:
    js_list = []

for arg in sys.argv[1:]:
    js_list.append(arg)
save_to_json_file(js_list, "add_item.json")
