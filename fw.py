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
    path = []
    
    state = problem.initial
    path.append(state)
    frontier.append(path)

    while(1):
        if len(frontier):
            #Election
            path = problem.criteria(frontier)
            state = path[len(path)-1]
            explored.append(state)
            frontier.remove(path)
            #new state

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
