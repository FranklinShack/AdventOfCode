def readFile(file):
    f = open(file)
    f = f.read().splitlines()

    #make ints
    new = []
    new2=[]
    
    for i in f:
        new.append(i.split(','))
    for i in new:
        temp=[]
        if i[0] == '' or i[0][0] not in '0123456789':
                break
        for j in i:
            print(j)
            temp.append(int(j))
        new2.append(temp)
    new2.append(list(new[-2][0][-3::2]))
    new2.append(list(new[-1][0][-3::2]))
    return new2
