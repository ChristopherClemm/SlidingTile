def printState(goal):
    for i in goal:
        print(i)
    print()
def left(goal, x, y):
    if y-1 >= 0:
        y = y-1
        temp = goal[x][y]
        goal[x][y] = 0
        goal[x][y+1] = temp
    printState(goal)

def right(goal, x, y):
    if y+1 <= 2:
        y = y+1
        temp = goal[x][y]
        goal[x][y] = 0
        goal[x][y-1] = temp
    printState(goal)
def down(goal, x, y):
    if x+1 <= 2:
        x = x+1
        temp = goal[x][y]
        goal[x][y] = 0
        goal[x-1][y] = temp
    printState(goal)
def up(goal, x, y):
    if x-1 >= 0:
        x = x-1
        temp = goal[x][y]
        goal[x][y] = 0
        goal[x+1][y] = temp
    printState(goal)
