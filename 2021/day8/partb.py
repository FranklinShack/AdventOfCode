import sys, getopt
import re, functools
from readFile import readFile
from aocd import submit

def main(argv):
    L=[]
    usage=("Usage: "+sys.argv[0]+' {-p -s}')
    try:
        opts, args = getopt.getopt(argv, "hps")
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            return 0
        elif opt == '-p':
            L = readFile("puzzleInput.txt")
        elif opt == '-s':
            L = readFile("sampleInput.txt")
    solut=sol(L)
    print(solut)
    #submit(solut)
    return 0

def intersect(a,b):
    res = ""
    for i in a:
        if i in b and not i in res:
            res += i
    return res

def union(a, b):
    res=a

    for i in b:
        if not i in a:
            res += i
    return res

def dun(n,string,e):
    for i in n:
        if len(string) > len(e[i]) and len(e[i])!=0:
            e[i] = intersect(string, e[i])
        else:
            e[i] = union(string, e[i])
    return e


def sol(L):
    mapper = [['a',0],['b',1],['c',2],['d',3],['e',4],['f',5],['g',6]]
    numstemp = []
    ntt=[]
    nums = [[0,1,2,4,5,6], [2,5], [0,2,3,4,6], [0,2,3,5,6], [1,2,3,5],[0,1,3,5,6], [0,1,3,4,5,6],[0,2,5],[0,1,2,3,4,5,6],[0,1,2,3,5,6]]
    for i in nums:
        ntt=[]
        for j in i:
            ntt.append(str(j))
        numstemp.append(ntt)
    nums=numstemp

    
    sum=0
    for i in L:
        num=""
        possvals=[""]*7
        for j in range(0,15):
            if len(i[j])==2:
                possvals = dun([2,5],i[j],possvals)
            elif len(i[j])==3:
                possvals = dun([0,2,5],i[j],possvals)
            elif len(i[j])==4:
                possvals = dun([1,2,3,5],i[j],possvals)
        
        if(possvals[2]==possvals[5] and len(possvals[2])==2):
            for j in possvals[2]:
                for k in range(len(possvals)):
                    if k!=2 and k!=5:
                        possvals[k] = possvals[k].replace(j,'')

            for j in range(11):
                if len(i[j])==6:
                    if (possvals[2][0] in i[j]) and (possvals[2][1] not in i[j]):
                        possvals[5]=possvals[2][0]
                        possvals[2]=possvals[2][1]
                        break
                    elif (possvals[2][0] not in i[j]) and (possvals[2][1] in i[j]):
                        possvals[5]=possvals[2][1]
                        possvals[2]=possvals[2][0]
                        break

        for j in range(15):
            if len(i[j])==5 and possvals[2] in i[j] and possvals[5] not in i[j] and len(possvals[1])==2:
                if possvals[1][0] in i[j]:
                    possvals[1] = possvals[3][0]
                    possvals[3] = possvals[3][1]
                    break
                else:
                    possvals[1] = possvals[3][1]
                    possvals[3] = possvals[3][0]  
                    break   

            elif len(i[j])==5 and possvals[2] not in i[j] and possvals[5] in i[j] and len(possvals[1])==2:
                if possvals[1][0] in i[j]:
                    possvals[1] = possvals[3][0]
                    possvals[3] = possvals[3][1]
                    break
                else:
                    possvals[1] = possvals[3][1]
                    possvals[3] = possvals[3][0]   
                    break
        
        for j in range(15):
            if len(i[j])==6 and possvals[2] in i[j] and possvals[3] in i[j]:
                temp=i[j]
                for k in range(7):
                        temp=temp.replace(possvals[k], '')
                possvals[6] = temp
                break
        
        temp="abcdefg"
        
        for j in possvals:
            temp = temp.replace(j,'')
        possvals[4]=temp
    
        outvals = [""]*4
        for j in range(11,15):
            outvals[j-11] = i[j]
            for k in range(len(possvals)):
                outvals[j-11] = outvals[j-11].replace(possvals[k],str(k))
            for k in range(len(nums)):
                if all(x in nums[k] for x in list(outvals[j-11])) and all(x in list(outvals[j-11]) for x in nums[k]):
                    num+=str(k)

        sum+=int(num)
        


    return sum

if __name__ == "__main__":
   main(sys.argv[1:])