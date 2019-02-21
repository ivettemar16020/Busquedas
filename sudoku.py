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
                problem = Sudoku()
                problem.goal_test(sudo)
                self.grid(sudo)
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
        print("Initial state: \n")
        print('\n'.join([''.join(['{:4}'.format(item) 
            for item in row]) for row in matrix]))
        print("_______________")

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
        #(state + action) -> state'  
        pass

    def goal_test(self, matrix): 
        #[1, 2, 3, 4] appear exactly once in each row, column and box

        #row
        for x in range(DIM): 
            goal = NUMBERS
            for y in range(4): 
                if (matrix[x][y] in goal): 
                    goal.remove(matrix[x][y])
                if (len(goal) > 0): 
                    return False

        #column
        for x in range(DIM): 
            goal = NUMBERS
            for y in range(4): 
                if (matrix[y][x] in goal): 
                    goal.remove(matrix[y][x])
                if (len(goal) > 0): 
                    return False

        #box
        #box1.append(matrix[0], matrix[1], matrix[4], matrix[5])
        #box2.append(matrix[2], matrix[3], matrix[6], matrix[7])
        #box3.append(matrix[8], matrix[9], matrix[12], matrix[13])
        #box4.append(matrix[10], matrix[11], matrix[14], matrix[15])
        a, b, c, i= (0,)*4
        while (i < DIM): 
            if(i==1):
                a = 2
            else if (i==2): 
                a = 0
                b = 2
            else if (i==3):
                a = 2
                b = 2
            for x in range(DIM/2): 
                for y in range(DIM/2)
                    if (matrix[x+b][y+a] in goal): 
                        goal.remove(matrix[x+b][y+a])
            if(len(goal) != 0): 
                return False
        
        return True

    def process(self, available_path):
        "Define costs and heuristic"
        best_path = 0
        cost = 0
        for n in available_path: 
            state = n[len(n) -1 ]
            cost = 0

            #heuristic? 
        return best_path
        
        
sudok = Start()
sudok.entry()

