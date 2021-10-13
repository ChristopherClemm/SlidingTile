


goal = [[1,2,4],
        [4,5,6],
        [0,8,7]]

initial = [[],[],[]]

"""
nodes = make queue(makenode(inittalstate)
)
loop do
if emoty return false
node = remove front
if problem = goaltest succeds then return nodesnodes = queeung function node expand problme operators

"""






#need left
#need right
#need up
#need down
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

def findIndexOfZero(goal):
    arr = [0,0]
    for i in range(len(goal)):
        for j in range(len(goal[0])):
            if goal[i][j] == 0:
                arr = [i,j]
                return arr
    return arr


def main():
    #input ur list
    #which opition do you want to choose

    arr = findIndexOfZero(goal)
    x = arr[0]
    y = arr[1]
    print(x,y)
    printState(goal)
    left(goal, 2, 0)
    right(goal,2,0)
    up(goal,2,1 )
    down(goal,1, 1)
    print("hi")

main()
