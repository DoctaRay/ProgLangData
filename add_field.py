import json
import os

filename = 'data_copy.json'

field = input("Enter a field name: ")
val = int(input("String (1) or String array (2)?: "))

def add_string(lang):
    tmp = lang
    tmp[field] = "Not updated"
    return tmp

def add_array(lang): 
    tmp = lang
    tmp[field] = ["Not updated"]
    return tmp

with open(filename, "r") as f:
    data = json.load(f)
    if val == 1:
        data = list(map(add_string, data))
    elif val == 2:
        data = list(map(add_array, data))
    else: 
        print("You must choose either a string or string array value for your field.")

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)