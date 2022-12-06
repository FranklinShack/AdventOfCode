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
            print(L)
        elif opt == '-r':
            submitFlag = True
    solution=solve(L)
    print(solution)

    if submitFlag:
        submit(solution)

    return 0

def solve(L):
    answer = 4
    str = L[0]

    for i in list(range(len(str)))[3::]:
        if len(set(list(str[i-3:i+1])))==4:
            return answer
        answer+=1


    return answer

if __name__ == "__main__":
   main(sys.argv[1:])