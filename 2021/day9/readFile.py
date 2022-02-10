def readFile(file):
    f = open(file)
    f = f.read().splitlines()

    #make ints
    new = []
    for i in f:
        new2=[]
        for j in i:
            new2.append(int(j))
        new.append(new2)
    return new
