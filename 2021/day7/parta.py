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
    submit(solut)

    return 0

def sol(L):
    pos=[]
    cost=[]
    for i in range(max(L)+1):
        pos.append(L.count(i))
        cost.append(0)

    for i in range(len(pos)):
        for j in range(len(pos)):
            cost[i]+=abs(i-j)*pos[j]

    return min(cost)

if __name__ == "__main__":
   main(sys.argv[1:])