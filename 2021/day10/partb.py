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
    scores=[]
    dict = {"(": [0, 1, ")"], "[": [1, 1, "]"], "{": [2, 1, "}"], "<": [3, 3, ">"], ")": [0,-1, 1], "]": [1, -1, 2], "}": [2,-1, 3], ">": [3, -1, 4]}

    for i in L:
        last=[]
        score=0
        cor=False
        for j in i:
            val = dict[j]
            if(val[1] > 0):
                last.append(val[2])
                continue
            if(j!=last[-1]):
                cor=True
                break
            last.pop()
        
        if(cor==False):
            for j in last[::-1]:
                score*=5
                score+= dict[j][2]
            if(score>0):
                scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

if __name__ == "__main__":
   main(sys.argv[1:])