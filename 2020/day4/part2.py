import sys, getopt
import re, functools
from readFile import readFile

def main(argv):
    L=[]
    try:
        opts, args = getopt.getopt(argv, "hps")
    except getopt.GetoptError:
        print('usage: part2.py {-p|-s}')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: part2.py {-p|-s}')
            return 0
        elif opt == '-p':
            L = readFile("puzzleInput.txt")
        elif opt == '-s':
            L = readFile("sampleInput.txt")
    print (sol(L))
    return 0

def hgt(s):
    if s[-2:] == "cm":
        return (int(s[:-2]) >= 150 and int(s[:-2]) <= 193)
    elif s[-2:] == "in":
        return (int(s[:-2]) >= 59 and int(s[:-2]) <= 76)
    else:
        return False

def hcl(s):
    if(s[0]!="#" and len(s)!=7):
        return False
    else:
        for i in s[1:]:
            if str(i) not in "0123456789abcdef":
                return False
    return True

def pid(s):
    if len(s)!=9:
        return False
    else:
        for i in s:
            if i not in "0123456789":
                return False
    return True

def sol(L):
    valid=0
    
    for i in L:
        print(i)
        cond=0
        for j in range(0, len(i), 2):
            cond += 1 if (i[j]=="byr" and int(i[j+1])>=1920 and int(i[j+1])<=2002) else 0
            cond += 1 if (i[j]=="iyr" and int(i[j+1])>=2010 and int(i[j+1])<=2020) else 0
            cond += 1 if (i[j]=="eyr" and int(i[j+1])>=2020 and int(i[j+1])<=2030) else 0
            cond += 1 if (i[j]=="hgt" and hgt(i[j+1])) else 0
            cond += 1 if (i[j]=="hcl" and hcl(i[j+1])) else 0
            cond += 1 if (i[j]=="ecl" and any(x in i[j+1] for x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])) else 0
            cond += 1 if (i[j]=="pid" and pid(i[j+1])) else 0       
        valid += (cond//7)
    return valid







if __name__ == "__main__":
   main(sys.argv[1:])