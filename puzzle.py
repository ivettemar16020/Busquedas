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
    '13','14','15','.'
]

class Start:
    def entry(self):
        """ User entry"""
        puz = []
        while True:
            temp = input("Enter 15Puzzle in Hexadecimal Format: ")
            if (len(temp) != 16): 
                print("Length must be 16 :(")
                return -1
            for i in temp:
                if (i == "."): 
                    puz.append("0")
                else: 
                    temp_dec = int(i, 16)
                    puz.append(str(temp_dec))
            print(puz)
            #problem = Puzzle()
            #problem.init = puz

            #response = fw.graph_search(problem)

            #if (response == False):
                #print(response)
            break

class Puzzle: 
    init = "Initial state"

    def goal_test(self, dim): 
        matrix = np.zeros((dim,dim))
        arrval = 1
        for x in range(dim):
            for y in range (dim):
                if(y == dim-1 and x == dim-1):
                    matrix[x,y] = 0
                else:
                    matrix[x,y] = arrval
                    arrval = arrval +1
        return matrix

    def process(self): 
        pass