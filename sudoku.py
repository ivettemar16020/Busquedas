"""
    UVG
    Ivette Cardona - 16020
    sudoku.py
    Style: PEP8  -   https://www.python.org/dev/peps/pep-0008/
"""

import copy
import fw 
import numpy as np

BLANK = 0
SPACE = " "
LINE = "|"
ROW = "-------------------------------------"
NUMBERS = ["1", "2", "3", "4"]
DIM = 4

class Start: 
    def entry(self):
        while True:
            temp = input("Sudoku(input) ")
            if (len(temp) != 16):
                print('Sudoku must be 4x4 (16 char) \nTry again :) \n')
            else: 
                sudo = self.sudoku_matrix(temp)
                print("Initial state: \n", sudo)
                break

    def sudoku_matrix(self, input): 
        row = []
        sudoku = []
        n = 0
        for i in input: 
            row.append(i)
            n += 1 
            if (n%DIM == 0):
                sudoku.append(row)
                row = [] #clean row
        return sudoku
    
    def grid(self, matrix):
        pass

class Sudoku: 

    initial = "Initial state"

    def actions(self, matrix): 
        empty = 0
        n = 0
        m = 0
        position = []
        possibility = []
        poss_matrix = []

        #Count of empty spaces
        for x in range(DIM):
            for y in range(DIM): 
                if matrix[x][y] == ".": 
                    position.append(tuple([x,y]))
                    empty += 1

        num = NUMBERS
        while(n < empty): 
            for i in range(DIM): 
                if ((matrix[position[n][0]][i] != ".") and (matrix[position[n][0]][i] in num)): 
                    num.remove(matrix[position[n][0]][i])
                    
            for i in range(DIM):
                 if ((matrix[i][position[n][1]] != ".") and (matrix[i][position[n][1]] in num)): 
                    num.remove(matrix[i][position[n][1]])
            
            possibility.append(num)
            n += 1
        
        while(m < empty): 
            for i in possibility[m]: 
                temp = copy.deepcopy(matrix)
                temp[position[m][0]][position[m][1]] = i
                poss_matrix.append(temp)
            m += 1

        return poss_matrix 

    
    def result(self):
        pass

    def goal_test(self, matrix): 
        #revisar que en cada fila, columna y cuadro 
        #se tengan los números 1, 2, 3, 4 
        pass

    def stepCost(self):
        pass

    
    def pathCost(self):
        pass


    def process(self):
        print("Enter the start state matrix \n")
        
        
sudok = Start()
sudok.entry()
