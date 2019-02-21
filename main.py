"""
    UVG
    Ivette Cardona - 16020
    main.py
    Style: PEP8  -   https://www.python.org/dev/peps/pep-0008/
"""

import sudoku as sudo 
#import puzzle as puz

def main(): 
    print("Graph-Search ~ Problem solver")
    while(1): 
        choice = input("Sudoku or 15Puzzle? (s - p - q)")
        if (choice == "s" or choice == "p" or choice == "q"): 
            print ("Your choice is: ", choice )
            if(choice == "s"): 
                sudoku = sudo.Start()
                sudoku.entry()
            if(choice == "p"):
                print("no")
                #fifteen = puz.Start()
                #fifteen.entry()
            if(choice == "q"): 
                print("Bye bye")
                break
        else: 
            print("Try again :(")
            

main()