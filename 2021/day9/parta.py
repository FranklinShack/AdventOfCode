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

def findBasin(L,i,j,visited):    
    visited.append([i,j])

    temp=list()
    [temp.append(item) for item in visited if item not in temp]
    visited=temp


    if j-1 >= 0 and L[i][j-1] > L[i][j] and (L[i][j-1]!=9) and [i,j-1] not in visited:
        visited += findBasin(L,i,j-1,visited)
    if j+1 < len(L[i]) and L[i][j+1] > L[i][j] and (L[i][j+1]!=9) and [i,j+1] not in visited:
        visited += findBasin(L,i,j+1,visited)
    if i-1 >= 0 and L[i-1][j] > L[i][j] and (L[i-1][j]!=9) and [i-1,j] not in visited:
        visited += findBasin(L,i-1,j,visited)
    if i+1 < len(L) and L[i+1][j] > L[i][j] and (L[i+1][j]!=9) and [i+1,j] not in visited:
        visited += findBasin(L,i+1,j,visited)
    return visited
     




def sol(L):
    sum=1
    basins=[]
    for i in range(len(L)):
        for j in range(len(L[i])):
            val = L[i][j]+1
            mini=val
            if j-1 >= 0:
                mini = min(mini, L[i][j-1])
            if j+1 < len(L[i]):
                mini = min(mini, L[i][j+1])
            if i-1 >= 0:
                mini = min(mini, L[i-1][j])
            if i+1 < len(L):
                mini = min(mini, L[i+1][j])
            if mini == val:
                vis=findBasin(L,i,j,[])
                temp=list()
                [temp.append(item) for item in vis if item not in temp]
                basins.append(len(temp))
                
                
                
    for i in range(3):
        print(basins)
        sum*=max(basins)
        basins.remove(max(basins))
    return sum

if __name__ == "__main__":
   main(sys.argv[1:])