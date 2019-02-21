"""
    UVG
    Ivette Cardona - 16020
    puzzle.py
    Style: PEP8  -   https://www.python.org/dev/peps/pep-0008/
"""

import ast
import fw
import math
import numpy as np 

GOAL = [
    '1','2','3','4',
    '5','6','7','8',
    '9','10','11','12',
    '13','14','15','_'
]

class Node:
    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval

    def movement(self, puzzle, x1, x2, y1, y2): 
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = puzzle.copy()
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

class Puzzle: 
    def __init__(self):
        self.open = []
        self.closed = []

    def entry(self):
        """ User entry"""
        puz = []
        temp = input("Enter 15Puzzle in Hexadecimal Format: ")
        if (len(temp) != 15): 
            print("Lenght must be 15 :(")
            return -1
        for i in range(len(temp) ):
            temp_dec = int(temp[i], 16)
            puz.append(str(temp_dec))
        print(puz) 
        return puz

    def heuristic(self, start, goal):
        pass

    def process(self):
        print("Enter 15Puzzle: \n")
        start = self.entry()