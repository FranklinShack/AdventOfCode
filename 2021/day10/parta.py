import sys, getopt
import re, functools
from collections import defaultdict
from readFile import readFile
from aocd import submit

def main(argv):
    L=[]
    usage=("Usage: "+sys.argv[0]+' {-p -s}')
    try:
        opts, args = getopt.getopt(argv, "hps")
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
    solut=sol(L)
    print(solut)
    #submit(solut)

    return 0

def sol(L):
    sum=0
    dict = {"(": [0, 1, ")"], "[": [1, 1, "]"], "{": [2, 1, "}"], "<": [3, 3, ">"], ")": [0,-1, 3], "]": [1, -1, 57], "}": [2,-1, 1197], ">": [3, -1, 25137]}

    for i in L:
        last=[]
        counts = [0]*4
        for j in i:
            val = dict[j]
            counts[val[0]] += val[1]

            if(val[1] > 0):
                last.append(val[2])
                continue
            if(j!=last[-1]):
                sum+=val[2]
                break
            last.pop()
    
    return sum

if __name__ == "__main__":
   main(sys.argv[1:])