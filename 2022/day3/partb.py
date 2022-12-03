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
    print(L)
    for x in list(range(len(L)))[::3]:
        s1 = L[x]
        s2 = L[x+1]
        s3 = L[x+2]
        item = list(set(s1).intersection(set(s2).intersection(set(s3))))[0]


        if item in LETTERS_LOWER:
            answer += LETTERS_LOWER.index(item)+1
        elif item in LETTERS_UPPER:
            answer += LETTERS_UPPER.index(item)+27

    return answer

if __name__ == "__main__":
   main(sys.argv[1:])