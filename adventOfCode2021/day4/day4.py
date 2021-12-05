import re
def readFile():
    f = open("adventOfCode2021/day4/ex.txt")
    f = f.read().split("\n\n")

    new = []
    for i in f:
        new.append(re.split('  |,|\n |\n| ',i))
    return new


def part1():
    winNum=0
    boards=readFile()
    won=[]
    for i in boards[0]:
        for j in range(len(boards)-1):
            for k in range(len(boards[1])):
                if i == boards[j+1][k]:
                    if "" in boards[j+1]:
                        boards[j+1].remove("")
                    winNum=i
                    print("---")
                    print(boards[j+1])
                    boards[j+1][k] = "X"
                    print(boards[j+1])
                    print("---")
                    if(checkWin(boards[j+1]) and boards[j+1] not in won):
                        won.append(boards[j+1])
                        if(len(won)==len(boards)-1):
                            print(winNum)
                            print(unmarked(won[99]))
                            return int(winNum)*unmarked(won[99])
    return True

def checkWin(board):
    for i in range(5):
        if board[i*5:(i*5)+5]==['X', 'X', 'X', 'X', 'X'] or (str(board[i])+str(board[i+5])+str(board[i+10])+str(board[i+15])+str(board[i+20]))=="XXXXX":
            return True
    return False

def unmarked(board):
    sum=0
    if(board[0]==''):
        board=board[1:]
    for i in board:
        sum += int(i) if i!="X" else 0
    return sum
print(part1())

def part2():
    return True