# a1.py
import time
import sys
import math 
from search import *
from utils import *

# Question 1: Helper Functions
def make_rand_8puzzle():
    initial = tuple(shuffled((1, 2, 3, 4, 5, 6, 7, 8, 0)))
    puzzle = EightPuzzle(initial)
    if puzzle.check_solvability(puzzle.initial) == False:
        puzzle = make_rand_8puzzle()
    return puzzle

def display(state):
    for i in state:
        if (state.index(i) + 1) % 3 == 0:
            if i == 0:
                print("*")
            else:
                print(i)
        else:
            if i == 0:
                print("*", end=" ")
            else:
                print(i, end=" ")

# Question 2: Run A* with Statistics
def run_with_statistics():
    if len(sys.argv) != 10 and len(sys.argv) != 1:
        # 1. insert serveral digits but not exactly 9 digits (filename count as an extra digit), print the message
        print('You need to insert 9 numbers in order to calculate the statistics.')
    elif len(sys.argv) == 1:
        # 2. if no instance is given, creates the random instance 
        puzzle = make_rand_8puzzle()
        display(puzzle.initial)
        print("Puzzle is solvable?", puzzle.check_solvability(puzzle.initial))

        print('Run a* with the misplaced-tiles heuristic')
        start_time = time.time()
        astar_search(puzzle, puzzle.h, True)
        elapsed_time = time.time() - start_time
        print(f'elapsed time(in seconds): {elapsed_time}s')

        print('\n')

        print('Run a* with the manhattan distance heuristic')
        start_time = time.time()
        astar_search(puzzle, manhattan, True)
        elapsed_time = time.time() - start_time
        print(f'elapsed time(in seconds): {elapsed_time}s')

        print('\n')

        print('Run a* with the gaschnig\'s heuristic')
        start_time = time.time()
        astar_search(puzzle, gaschnig, True)
        elapsed_time = time.time() - start_time
        print(f'elapsed time(in seconds): {elapsed_time}s')
    else:
        # 3. insert 9 digits
        initial = tuple(list(map(int, sys.argv[1:])))
        puzzle = EightPuzzle(initial)
        display(puzzle.initial)

        if puzzle.check_solvability(puzzle.initial):
            print("Puzzle is solvable?", puzzle.check_solvability(puzzle.initial))
            print('Run a* with the misplaced-tiles heuristic')
            start_time = time.time()
            astar_search(puzzle, puzzle.h, True)
            elapsed_time = time.time() - start_time
            print(f'elapsed time(in seconds): {elapsed_time}s')

            print('\n')

            print('Run a* with the manhattan distance heuristic')
            start_time = time.time()
            astar_search(puzzle, manhattan, True)
            elapsed_time = time.time() - start_time
            print(f'elapsed time(in seconds): {elapsed_time}s')

            print('\n')

            print('Run a* with the gaschnig\'s heuristic')
            start_time = time.time()
            astar_search(puzzle, gaschnig, True)
            elapsed_time = time.time() - start_time
            print(f'elapsed time(in seconds): {elapsed_time}s')
        else:
            print("Your input case is not solvable, try another one!")

# Question 3: Manhattan Distance Heuristic
def manhattan(n):
    distance = 0
    initial_state = n.state
    goal_state = (1,2,3,4,5,6,7,8,0)
    if initial_state != goal_state:
        for i in range(len(goal_state)):
            point1 = manhattan_helper(initial_state.index(i))
            point2 = manhattan_helper(goal_state.index(i))
            value = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
            distance += value
    return distance

def manhattan_helper(index):
    x = math.floor(index/3)
    y = index%3
    return (x,y)

# Question 4: Gaschnig’s Heuristic
def gaschnig(n):
    moves = 0
    initial_state = list(n.state)
    goal_state = list((1,2,3,4,5,6,7,8,0))
    if initial_state != goal_state:
        while initial_state != goal_state:
            if initial_state.index(0) == goal_state.index(0):
                index = 0
                value = 0
                for i in range(len(goal_state)):
                    if initial_state.index(i) != goal_state.index(i):
                        index = initial_state.index(i)
                        value = i
                        break
                initial_state[initial_state.index(0)] = value
                initial_state[index] = 0
            else:
                value = goal_state[initial_state.index(0)] 
                index = initial_state.index(value)
                initial_state[initial_state.index(0)] = value
                initial_state[index] = 0
            moves += 1
    return moves


def main():
    # puzzle = make_rand_8puzzle()
    # display((0, 3, 2, 1, 8, 7, 4, 6, 5))
    # display(puzzle.initial)
    # for i in range(9):
    #     print(manhattan_helper(i))
    run_with_statistics()
    # for i in range(9):
    #     run_with_statistics()

if __name__ == "__main__":
    main()