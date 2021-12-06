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

def sol(L):
    for i in range(80):
        #print("After "+str(i)+"days:" + str(L))
        for j in range(len(L)):
            if(L[j]==0):
                L[j] = 6
                L.append(8)
            else:
                L[j] = L[j]-1
    return len(L)







if __name__ == "__main__":
   main(sys.argv[1:])