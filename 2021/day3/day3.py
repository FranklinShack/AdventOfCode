def readFile():
    f = open("adventOfCode2021/day3/ex.txt")
    f = f.read().splitlines()
    return f
    new = []
    for i in f:
        new.append(i.split(','))
    return new


def dayThree1():
    L = readFile()
    l=[0,0]
    gamma=""
    epsilon=""
    print(L[0][1])
    for i in range(len(L[0])):
        l=[0,0]
        for j in range(len(L)):
            l[int(L[j][i])]+=1
        if(l[0]>l[1]):
            gamma+=str(0)
            epsilon+=str(1)
        else:
            gamma+=str(1)
            epsilon+=str(0)
    return int(gamma,2)*int(epsilon,2)

def member(a, b):
    return a in b

def dayThree2():
    L = readFile()
    oxL=L
    coL=L
    comp=0
    index=0
    while(len(oxL)>1):
        l=[0,0]
        for i in range(len(oxL)):
            l[int(oxL[i][index])]+=1
        if(l[0]>l[1]):
            comp=0
        else:
            comp=1
        oxL=list(filter(lambda s: int(s[index])==comp, oxL))
        index+=1
    index=0
    while(len(coL)>1):
        l=[0,0]
        for i in range(len(coL)):
            l[int(coL[i][index])]+=1
        if(l[0]<=l[1]):
            comp=0
        else:
            comp=1
        coL=list(filter(lambda s: int(s[index])==comp, coL))
        index+=1
        
    print(oxL)
    print(coL)
    return int(oxL[0],2)*int(coL[0],2)
print(dayThree2())