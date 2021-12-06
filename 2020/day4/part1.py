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
    count=0
    for i in L:
        count+=1 if (all(x in str(i) for x in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))) else 0
    return count



if __name__ == "__main__":
   main(sys.argv[1:])