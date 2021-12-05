def inputa():
       f = open("ex.txt")
       f = f.read().splitlines()
   
       #make ints
       new = []
       for i in f:
           new.append(int(i))
       return new

def advent1():
    L=inputa()
    count=0
    for a in range(1, len(L)):
        if(L[a] > L[a-1]):
            count+=1
    return count

def advent2():
    L=inputa()
    count=0
    window1=L[0]+L[1]+L[2]
    for a in range(1,len(L)-2):
        window2=L[a]+L[a+1]+L[a+2]
        if window2 > window1:
            count+=1
        window1=window2
    return count

print(advent1())
print(advent2())
