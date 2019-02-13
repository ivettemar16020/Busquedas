"""
    UVG
    Ivette Cardona - 16020
    sudoku.py
    Style: PEP8  -   https://www.python.org/dev/peps/pep-0008/
"""

import numpy as np

blank = 0
space = " "
line = "|"
row = "-------------------------------------"

dim = int(input("¿Dimensiones del sudoku? "))
#Inicializar matriz de dimxdim con ceros
mat = np.zeros ((dim,dim))

problem = input("Ingrese el sudoku que desea resolver: ")

#Llenando matriz 
for i in range(dim): 
    if(problem[i] == "."):
        mat[i] = 0
    else: 
        mat[i] = (int)(problem[i])

print(mat)

"""
def show_grid(int grid[dim][dim]):
    for i in range(0,dim):
        print(blank)
"""