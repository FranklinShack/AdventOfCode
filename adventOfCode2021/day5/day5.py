import re
DIR_PATH="adventOfCode2021/day5/"
def readFile():
    f = open(DIR_PATH+"ex.txt")
    f = f.read().split("\n")

    new = []
    for i in f:
        new.append(i.split(" -> "))
    
    new2 = []
    for i in new:
        temp=[]
        for j in i:
            temp.append(j.split(","))
        new2.append(temp)
    return new2


def part1():
    L=readFile()
    grid=[]
    for i in range(1000):
        temp=[]
        for j in range(1000):
            temp.append(0)
        grid.append(temp)
    count=0
    for i in L:
        col0=int(i[0][1])
        col1=int(i[1][1])
        mincol = min(col0, col1)
        abscol=abs(col0-col1)
        row0=int(i[0][0])
        row1=int(i[1][0])
        minrow = min(row0, row1)
        absrow = abs(row0-row1)

        if (row0==row1):
            for j in range(abscol+1):
                grid[mincol+j][row0] += 1

        elif (col0==col1):
            for j  in range(absrow+1):
                grid[col0][minrow+j] += 1

    for i in grid:
        for j in i:
            if j >= 2:
                count+=1
    return count

def part2():
    L=readFile()
    grid=[]
    for i in range(1000):
        temp=[]
        for j in range(1000):
            temp.append(0)
        grid.append(temp)
    count=0

    for i in L:
        col0=int(i[0][1])
        col1=int(i[1][1])
        mincol = min(col0, col1)
        abscol=abs(col0-col1)
        row0=int(i[0][0])
        row1=int(i[1][0])
        minrow = min(row0, row1)
        absrow = abs(row0-row1)

        if (row0==row1):
            for j in range(abscol+1):
                grid[mincol+j][row0] += 1

        elif (col0==col1):
            for j  in range(absrow+1):
                grid[col0][minrow+j] += 1
        else: 
            colstart = max(col0,col1) if col0 < col1 else mincol
            colinc = -1 if col0 < col1 else 1
            rowstart = max(row0,row1) if row0 < row1 else minrow 
            rowinc = -1 if row0 < row1 else 1
            for j in range(absrow+1):
                grid[colstart+(colinc*j)][rowstart+(rowinc*j)] += 1

    for i in grid:
        for j in i:
            if j >= 2:
                count+=1
    return count


print("|---------------|")
print("|Part 1:        |")
print("|"+str(part1()))
print("|---------------|")
print("|Part 2:        |")
print("|"+str(part2()))
print("|---------------|")