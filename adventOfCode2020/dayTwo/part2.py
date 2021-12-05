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
    print (sol(L))
    return 0

def xor(x, y):
    return bool((x and not y) or (not x and y))

def sol(L):
    valid=0
    for i in L:
        i[0],i[1]=int(i[0]),int(i[1])
        password = i[3]
        token = i[2]
        if xor(password[i[0]-1]==token,password[i[1]-1]==token):
            valid+=1
    return valid




if __name__ == "__main__":
   main(sys.argv[1:])