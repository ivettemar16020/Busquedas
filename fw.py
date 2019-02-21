"""
    UVG
    Ivette Cardona - 16020
    fw.py
    Style: PEP8  -   https://www.python.org/dev/peps/pep-0008/
"""
import copy

#Code from: Samuel Chavez 

def graph_search(problem):
    frontier = []
    explored = []
    path = [] #Result from A*
    
    state = problem.init
    path.append(state)
    frontier.append(path)

    while(1):
        if len(frontier):
            #Election
            path = problem.process(frontier)
            state = path[len(path)-1]
            explored.append(state)
            frontier.remove(path)
            #new state
            print_state(state)

            #Test
            if problem.goal_test(state):
                return path

            #Expansion
            probability = problem.actions(state)
            for i in probability:
                if i not in explored: 
                    new_path = copy.deepcopy(path)
                    new_path.append(i)
                    frontier.append(new_path)

        else: 
            return False

def print_state(matrix):
        print('\n'.join([''.join(['{:4}'.format(item) 
            for item in row]) for row in matrix]))
        print("_______________")