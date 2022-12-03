import sys, getopt
sys.path.append('../../..')
import re, functools, itertools, collections, math
from AdventOfCode.aocUtils import *
from aocd import submit
import readFile as rf

def main(argv):
    L=[]
    submitFlag = False
    usage=("Usage: "+sys.argv[0]+' {-p -s -r}')
    try:
        opts, args = getopt.getopt(argv, "hpsr")
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            return 0
        elif opt == '-p':
            L = rf.readFile("puzzleInput.txt")
        elif opt == '-s':
            L = rf.readFile("sampleInput.txt")
        elif opt == '-r':
            submitFlag = True
    solution=solve(L)
    print(solution)

    if submitFlag:
        submit(solution)

    return 0

def solve(L):
    answer = 0

    x_coords = []
    y_coords = []

    for i in range(len(L)-2):
        x_coords.append(L[i][0])
        y_coords.append(L[i][1])

    max_x = max(x_coords)
    max_y = max(y_coords)

    grid = []

    for y in range(max_y+1):
        row = []
        for x in range(max_x+1):
            row.append('.')
        grid.append(row)


    for i in range(len(L)-2):        
        grid[L[i][1]][L[i][0]] = '#'

    fold_line = int(L[-2][1])
    top_half = grid[:fold_line]
    bottom_half = grid[fold_line::]

    bottom_half = flip_matrix_vertical(bottom_half)
    for y in range(len(top_half)):
        for x in range(len(top_half[0])):
            if(bottom_half[y][x] == '#' or top_half[y][x] == '#'):
                answer+=1


    return answer

if __name__ == "__main__":
   main(sys.argv[1:])