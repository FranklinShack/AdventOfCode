file=""
def readFile(file):
    f = open(file)
    f = f.read().splitlines()

    #make ints
    new = []
    for i in f:
        new.append(int(i))
    return new

def readFile(file):
    f = open(file)
    f = f.read().splitlines()
    
    new = []
    for i in f:
        new.append(i.split(' '))
    return new

#############################################
def readFile(file):
    f = open(fle)
    f = f.read().splitlines()
    
    new = []
    for i in f:
        new.append(i.split(' '))
    return new

##################################################
import re
def readFile(file):
    f = open(file).read()
    f = f.split("\n\n")

    new = []
    for i in f:
        new.append(re.split(' |\n',i))
    
    return new

###################################################
a=readFile()
print(readFile())
print(all (x in str(a[0]) for x in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')))


