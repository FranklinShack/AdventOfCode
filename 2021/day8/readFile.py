import re
def readFile(file):
    f = open(file).read()
    f = f.split("\n")

    new = []
    for i in f:
        new.append(re.split(' ',i))
    
    return new