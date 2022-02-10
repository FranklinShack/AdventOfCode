def readFile(file):
    f = open(file)
    f = f.read().splitlines()

    #make ints
    new = []
    for i in f:
        new.append(i.split('-'))
    return new
