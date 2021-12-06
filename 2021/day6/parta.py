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