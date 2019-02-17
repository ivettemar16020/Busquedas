"""
    UVG
    Ivette Cardona - 16020
    puzzle.py
    Style: PEP8  -   https://www.python.org/dev/peps/pep-0008/
"""

import ast
import math
import numpy as np 

class Node:
    def __init__(self,data,level,fvalue):
        self.data = data
        self.level = level
        self.fvalue = fvalue
    
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
