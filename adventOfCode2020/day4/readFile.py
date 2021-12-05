import re
def readFile(file):
    f = open(file).read()
    f = f.split("\n\n")

    new = []
    for i in f:
        new.append(re.split(' |\n',i))
    
    return new