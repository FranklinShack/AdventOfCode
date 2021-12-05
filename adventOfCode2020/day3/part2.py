import sys, getopt
import re, functools
from readFile import readFile

def main(argv):
    L=[]
    try:
        opts, args = getopt.getopt(argv, "hps")
    except getopt.GetoptError:
        print('usage: part2.py {-p|-s}')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: part2.py {-p|-s}')
            return 0
        elif opt == '-p':
            L = readFile("puzzleInput.txt")
        elif opt == '-s':
            L = readFile("sampleInput.txt")
    print (sol(L))
    return 0

def sol(L):
    treeCountMult=1
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    for i in slopes:
        treeCountMult *= checkSlope(L, i[0], i[1])
    return treeCountMult

def checkSlope(L, xInc, yInc):
    x=0
    treeCount=0
    for i in range(0, len(L), yInc):
        if L[i][x]=="#":
            treeCount+=1
        x = (x+xInc) % (len(L[i]))
    print(treeCount)
    return treeCount




if __name__ == "__main__":
   main(sys.argv[1:])