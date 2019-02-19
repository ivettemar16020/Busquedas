"""
    UVG
    Ivette Cardona - 16020
    puzzle.py
    Style: PEP8  -   https://www.python.org/dev/peps/pep-0008/
"""

import ast
import math
import numpy as np 

GOAL = [
    '1','2','3','4',
    '5','6','7','8',
    '9','A','B','C',
    'D','E','F','_'
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
        """ Entrada de usuario """
        puz: []
        temp = input()
        puz = list(temp)

        print(puz) 
        return puz

    def process(self):
        print("Entre el 15p a resolver: \n")
        start = self.entry()

fifteen = Puzzle()
fifteen.process()
