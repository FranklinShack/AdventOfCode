import sys, getopt
import re, functools
from readFile import readFile

def main(argv):
    L=[]
    try:
        opts, args = getopt.getopt(argv, "hps")
    except getopt.GetoptError:
        print ('part1.py -p | -s')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('part1.py -p | -s')
            return 0
        elif opt == '-p':
            L = readFile("puzzleInput.txt")
        elif opt == '-s':
            L = readFile("sampleInput.txt")
    print (part2(L))
    return 0

def part2(L):
    return 0





if __name__ == "__main__":
       main(sys.argv[1:])