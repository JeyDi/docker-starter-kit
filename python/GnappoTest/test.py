#!/usr/bin/env python
from time import sleep
import sys
import json
import random as rd


def test(data):
    sleep(10)
    a = data["a"]
    b = data["b"]
    print(f"a: {a}, b: {b}")
    return a + b + rd.random()

def read_file(path):
    
    # Opening JSON file
    f = open(path)
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    print(data)
    
    # Closing file
    f.close()
    
    return data

def save_to_file(dict):
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    path = str(sys.argv[1]) #take all the file path (with filename)
    print(f"Starting the test")
    data = read_file(path)
    sum = test(data)
    result = {"sum": sum} 
    save_to_file(result)
    print(f"test finish: {result}")
    
    