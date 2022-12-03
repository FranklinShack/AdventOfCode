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

    oppLets = ['A', 'B', 'C']
    meLets  = ['X', 'Y', 'Z']
    outcome = 0
    me = ''
    opp = ''
    for x in L:
        opp = x[0]
        me = x[2]
        if meLets.index(me) == oppLets.index(opp):
            outcome = 3
        if ((me == 'X' and opp == 'B') or (me == 'Y' and opp == 'C') or (me == 'Z' and opp == 'A')):
            outcome = 0
        elif((me == 'X' and opp == 'C') or (me  == 'Y' and opp == 'A') or (me == 'Z' and opp == 'B')):
            outcome = 6
        answer += outcome + meLets.index(me) + 1
    return answer

if __name__ == "__main__":
   main(sys.argv[1:])