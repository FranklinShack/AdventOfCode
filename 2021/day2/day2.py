def readFile():
    f = open("adventOfCode2021/dayTwo/ex.txt")
    f = f.read().splitlines()
    
    new = []
    for i in f:
        new.append(i.split(' '))
    return new

def sub():
    L = readFile()
    hor=0
    ver=0

    for i in L:
        if i[0]=="forward":
            hor+=int(i[1])
        elif i[0]=="up":
            ver-=int(i[1])
        elif i[0]=="down":
            ver+=int(i[1])
    return hor*ver

def sub2():
    L = readFile()
    aim=0
    hor=0
    ver=0

    for i in L:
        if i[0]=="forward":
            hor+=int(i[1])
            ver+= int(i[1])*aim
        elif i[0]=="up":
            aim-=int(i[1])
        elif i[0]=="down":
            aim+=int(i[1])
    return hor*ver


print(sub2())

