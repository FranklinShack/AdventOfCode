def readFile(file):
    f = open(file)
    f = f.read().splitlines()

    #make ints
    new = []
    new2=[]
    
    for i in f:
        new.append(list(i))
    for i in new:
        temp=[]
        for j in i:
            temp.append(int(j))
        new2.append(temp)
    return new2
