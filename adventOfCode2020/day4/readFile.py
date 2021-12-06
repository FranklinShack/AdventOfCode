import re
def readFile(file):
    f = open(file).read()
    f = f.split("\n\n")

    new = []
    for i in f:
        new.append(re.split(' |\n',i))
    new2=[]
    for i in new:
        for j in i:
            new2.append(re.split(':', j))
    
    return new2