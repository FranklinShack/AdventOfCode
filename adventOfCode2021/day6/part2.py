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
    ar=[]
    for i in range(9):
        ar.append(L.count(i))
    for i in range(256):
        #print("After "+str(i)+"days:" + str(L))
        temp = ar[0]
        for i in range(8):
            ar[i]=ar[i+1]
        ar[6]+=temp
        ar[8]=temp
    sum=0
    for i in ar:
        sum+=i
    return sum






if __name__ == "__main__":
       main(sys.argv[1:])