def printState(initial):
    for i in initial:
        print(i)
    print()
    return
def left(initial, x, y):
    newArray = [list(row) for row in initial]
    if y-1 >= 0:
        y = y-1
        temp = newArray[x][y]
        newArray[x][y] = 0
        newArray[x][y+1] = temp
    #printState(newArray)
    return newArray

def right(initial, x, y):
    newArray = [list(row) for row in initial]
    if y+1 <= 2:
        y = y+1
        temp = newArray[x][y]
        newArray[x][y] = 0
        newArray[x][y-1] = temp
    #printState(initial)
    return newArray
def down(initial, x, y):
    newArray = [list(row) for row in initial]
    if x+1 <= 2:
        x = x+1
        temp = newArray[x][y]
        newArray[x][y] = 0
        newArray[x-1][y] = temp
    #printState(initial)
    return newArray
def up(initial, x, y):
    newArray = [list(row) for row in initial]
    if x-1 >= 0:
        x = x-1
        temp = newArray[x][y]
        newArray[x][y] = 0
        newArray[x+1][y] = temp
    #printState(initial)
    return newArray
