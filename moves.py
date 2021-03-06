#used for printing out state in nice format
def printState(initial):
    for i in initial:
        print(i)
    print()
    return
#copies input and manipluates it with a left move desired
def left(initial, x, y):
    #used for coping the array because Python uses pass by object instead of pass by value
    newArray = [list(row) for row in initial]
    if y-1 >= 0:
        y = y-1
        temp = newArray[x][y]
        newArray[x][y] = 0
        newArray[x][y+1] = temp
    #printState(newArray)
    return newArray
#copies input and manipluates it with a right move desired

def right(initial, x, y):
    newArray = [list(row) for row in initial]
    if y+1 <= 2:
        y = y+1
        temp = newArray[x][y]
        newArray[x][y] = 0
        newArray[x][y-1] = temp
    #printState(initial)
    return newArray
#copies input and manipluates it with a down move desired

def down(initial, x, y):
    newArray = [list(row) for row in initial]
    if x+1 <= 2:
        x = x+1
        temp = newArray[x][y]
        newArray[x][y] = 0
        newArray[x-1][y] = temp
    #printState(initial)
    return newArray

#copies input and manipluates it with a up move desired

def up(initial, x, y):
    newArray = [list(row) for row in initial]
    if x-1 >= 0:
        x = x-1
        temp = newArray[x][y]
        newArray[x][y] = 0
        newArray[x+1][y] = temp
    #printState(initial)
    return newArray
