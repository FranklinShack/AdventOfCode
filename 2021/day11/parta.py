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

def flashAdj(L, y, x):
    for i in range(max(0, y-1), min(len(L), y+2)):
        for j in range(max(0, x-1), min(len(L[i]), x+2)):
            if L[i][j] > 0 and L[i][j] < 10:
                L[i][j]+=1
    return L

def sol(L):
    print(L)
    flashes=0
    for step in range(10000):
        flashesThisStep=0
        for i in range(len(L)):
            for j in range(len(L[i])):
                if L[i][j]<=9:
                    L[i][j]+=1
        flashing=True
        while flashing:
            cont=False
            for i in range(len(L)):
                for j in range(len(L[i])):
                    if(L[i][j]>9):
                        L[i][j]=0
                        L=flashAdj(L,i,j)
                        flashes+=1
                        flashesThisStep+=1
                        cont=True
            if(flashesThisStep==(len(L)*len(L[1]))):
                return step+1
            if not cont:
                break
            
                
    print(L)
    return flashes

if __name__ == "__main__":
   main(sys.argv[1:])