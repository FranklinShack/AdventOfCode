import sys, getopt
sys.path.append('../../..')
import re, functools, itertools
from AdventOfCode.aocUtils import *
from aocd import submit

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
            L = readFile("puzzleInput.txt")
        elif opt == '-s':
            L = readFile("sampleInput.txt")
        elif opt == '-r':
            submitFlag = True
    solution=solve(L)
    print(solution)

    if submitFlag:
        submit(solution)

    return 0

def solve(L):
    answer = 0
    elves = []
    calSum = 0
    for cals in L:
        if cals == '':
            elves.append(calSum)
            calSum=0
        else:
            calSum += int(cals)
    elves.append(calSum)
    answer = max(elves)
    return answer

if __name__ == "__main__":
   main(sys.argv[1:])