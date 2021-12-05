import sys, getopt
import re, functools
from readFile import readFile

def main(argv):
    L=[]
    try:
        opts, args = getopt.getopt(argv, "hps")
    except getopt.GetoptError:
        print('usage: part1.py {-p|-s}')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: part1.py {-p|-s}')
            return 0
        elif opt == '-p':
            L = readFile("puzzleInput.txt")
        elif opt == '-s':
            L = readFile("sampleInput.txt")
    print (sol(L))
    return 0

def sol(L):
    
    x=0
    treeCount=0
    for i in L:
        if i[x]=="#":
            treeCount+=1
        x = (x+3) % (len(i))
    return treeCount



if __name__ == "__main__":
   main(sys.argv[1:])