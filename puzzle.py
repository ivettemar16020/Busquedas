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
            problem = Puzzle()
            problem.init = puz

            response = fw.graph_search(problem)

            if (response == False):
                print(response)
            break
"""
    def create_matrix(self, dim, arr):
        matrix = np.zeros((dim,dim))
        arrval = 0
        for x in range(dim):
            for y in range (dim):
                matrix[x,y] = arr[arrval]
                arrval = arrval +1
        return matrix

    def blanknode(self, matrix, n, val):
        n = Node()
        for x in range(n):
            for y in range (n):
                value = matrix[x,y]
                if value == val:
                    return n.node(x,y)

class Node():
    def __init__(self,x,y):
        self.x = x
        self.y = y
"""
class Puzzle: 
    init = "Initial state"

    start = Start()
"""
    n = Node(0,0)

    def newFrontier(self, s,a):   
        vacio = start.blanknode(s,4,0)
        if(a == "arriba"):
            return n.node(vacio.x-1,vacio.y)                        
        if(a == "abajo"):
            return n.node(vacio.x+1,vacio.y)         
        if(a == "izquierda"):
            return n.node(vacio.x,vacio.y-1)       
        if(a == "derecha"):
            return n.node(vacio.x,vacio.y+1) 

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
        pass"""