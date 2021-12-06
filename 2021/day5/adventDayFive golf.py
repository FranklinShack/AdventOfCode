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

def makeGrid(n):
    grid=[]
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(0)
        grid.append(temp)
    return grid

def part1():
    L=readFile()
    grid=makeGrid(1000)
    count=0
    #----------------------------------------------------------------------#
    for i in L:
        col0,col1=int(i[0][1]),int(i[1][1])
        mincol,maxcol,abscol=min(col0, col1),max(col0, col1),abs(col0-col1)
        row0,row1=int(i[0][0]),int(i[1][0])
        minrow,maxrow,absrow=min(row0, row1),max(row0, row1),abs(row0-row1)
        if (row0==row1):
            for j in range(abscol+1):
                grid[mincol+j][row0] += 1

        elif (col0==col1):
            for j  in range(absrow+1):
                grid[col0][minrow+j] += 1
    #----------------------------------------------------------------------#
    for i in grid:
        for j in i:
            if j >= 2:
                count+=1
    return count

def part2():
    L=readFile()
    grid=makeGrid(1000)
    count=0
    #----------------------------------------------------#
    for i in L:
        col0,col1=int(i[0][1]),int(i[1][1])
        mincol,maxcol,abscol=min(col0, col1),max(col0, col1),abs(col0-col1)
        row0,row1=int(i[0][0]),int(i[1][0])
        minrow,maxrow,absrow=min(row0, row1),max(row0, row1),abs(row0-row1)
        if (row0==row1):
            for j in range(abscol+1):
                grid[mincol+j][row0] += 1
        elif (col0==col1):
            for j  in range(absrow+1):
                grid[col0][minrow+j] += 1
        else: 
            for j in range(absrow+1):
                grid[(maxcol if col0 < col1 else mincol)+((-1 if col0 < col1 else 1)*j)][(maxrow if row0 < row1 else minrow)+((-1 if row0 < row1 else 1)*j)] += 1
    #----------------------------------------------------#
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