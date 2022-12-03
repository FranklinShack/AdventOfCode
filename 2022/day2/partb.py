import sys, getopt
sys.path.append('../../..')
import re, functools, itertools, collections, math
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
    oppLets = ['C', 'B', 'A']
    meLets  = ['Z', 'Y', 'X']
    outcome = 0
    me = ''
    opp = ''
    for x in L:
        opp = x[0]
        me = x[2]

        if meLets.index(me) == oppLets.index(opp):
            outcome = abs(meLets.index(me)-2)*3 + (oppLets.index(opp))+1

        if ((me == 'X' and opp == 'B') or (me == 'Y' and opp == 'C')):
            outcome = abs(meLets.index(me)-2)*3 + (oppLets.index(opp)-1)%3 + 1

        elif( (me  == 'Y' and opp == 'A')):
            outcome = abs(meLets.index(me)-2)*3 + (abs(meLets.index(me)-2))
        elif (me == 'Z' and opp == 'B'):
            outcome = 9
        elif (me == 'X' and opp == 'C'):
            outcome = 2
        elif (me == 'Z' and opp == 'A'):
            outcome = 8
        print(outcome)
        answer += outcome
    
    return answer

if __name__ == "__main__":
   main(sys.argv[1:])