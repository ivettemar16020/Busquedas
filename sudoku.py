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
            if (n%4 == 0):
                sudoku.append(row)
                row = [] #clean row
        return sudoku

class Sudoku: 

    initial = "Initial state"

    def actions(self, matrix): 
        #rules 
        pass
    
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
