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
    ar = [L.count(0), L.count(1), L.count(2), L.count(3), L.count(4), L.count(5), L.count(6), L.count(7), L.count(8)]
    for i in range(256):
        #print("After "+str(i)+"days:" + str(L))
        temp = ar[0]
        ar[0]=ar[1]
        ar[1]=ar[2]
        ar[2]=ar[3]
        ar[3]=ar[4]
        ar[4]=ar[5]
        ar[5]=ar[6]
        ar[6]=ar[7]+temp
        ar[7]=ar[8]
        ar[8]=temp
    sum=0
    for i in ar:
        sum+=i
    return sum






if __name__ == "__main__":
       main(sys.argv[1:])