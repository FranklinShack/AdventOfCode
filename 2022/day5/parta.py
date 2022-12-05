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
    answer = ""
    towers = []
    instructions = []
    for str in L:
        if('[' in str):
            towerNum = 0
            for i in list(range(len(str)-1))[::4]:
                if towerNum <= len(towers):
                    towers.append([])
                if str[i+1] != ' ':
                    towers[towerNum].append(str[i+1])
                towerNum+=1
        elif 'm' in str:
            count = int(str[4:7])
            fromTower = int(str[12:14]) if  count < 10 else int(str[13:15])
            toTower = int(str[17:19]) if count < 10 else int(str[18:20])

            for i in range(count):
                towers[toTower-1].insert(0, towers[fromTower-1][0])
                del towers[fromTower-1][0]

    for tower in towers:
        if tower != []:
            answer += tower[0]
    return answer

if __name__ == "__main__":
   main(sys.argv[1:])