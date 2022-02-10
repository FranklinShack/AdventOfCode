import sys, getopt
import re, functools
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
    for i in range(len(L)):
        print("-----")
        print(len(L))
        print(len(L[i]))
        print(L[i])
        for j in range(10,15):
            print("--")
            print(j)
            sum+=1 if len(L[i][j]) in [2,3,4,7] else 0
    return sum

if __name__ == "__main__":
   main(sys.argv[1:])