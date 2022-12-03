import sys, getopt
sys.path.append('../../..')
import re, functools, itertools, collections, math
from AdventOfCode.aocUtils import *
from aocd import submit

def main(argv):
    L=[]
    submitFlag = False
    usage=("Usage: "+sys.argv[0]+' {-p -s -r}')
    try:
        opts, args = getopt.getopt(argv, "hpsr")
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
        elif opt == '-r':
            submitFlag = True
    solution=solve(L)
    print(solution)

    if submitFlag:
        submit(solution)

    return 0

def solve(L):
    answer = 0

    connections = []
    for connection in L:
        connections.append(connection.split('-'))

    nodes = []
    for connection in connections:
        nodes.append(connection[0])
        nodes.append(connection[1])
    nodes = sorted(list(set(nodes)))

    canVisit = []
    for node in nodes:
        lst = []
        for connection in connections:
            if(connection[0] == node):
                lst.append(connection[1])
            elif(connection[1] == node):
                lst.append(connection[0])
        canVisit.append(lst)
    
    visits = list(zip(nodes,canVisit))

    visitCounts = dict(zip(nodes, [0]*len(nodes)))
    print(visitCounts)

    def traverse(node, visitCounts, twice):
        nonlocal answer
        visitCounts[node] += 1

        if(node[0] in 'abcdefghijklmnopqrstuvwxyz' and visitCounts[node] == 2):
            twice = True

        if node == 'end':
            answer+=1
            return 0

        for nextNode in visits[nodes.index(node)][1]:
            
            if nextNode!='start' and (nextNode[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or visitCounts[nextNode] < 1 or (visitCounts[nextNode] < 2 and not twice)):
                traverse(nextNode, visitCounts.copy(), twice)
        return 0

    traverse('start', visitCounts.copy(), False)

    return answer

if __name__ == "__main__":
   main(sys.argv[1:])