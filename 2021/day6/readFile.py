def readFile(file):
    f = open(file)
    f = f.read().split(",")

    #make ints
    new = []
    for i in f:
        new.append(int(i))
    return new
