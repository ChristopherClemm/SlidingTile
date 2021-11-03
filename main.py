
import moves

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]



"""
nodes = make queue(makenode(inittalstate)
)
loop do
if emoty return false
node = remove front
if problem = goaltest succeds then return nodesnodes = queeung function node expand problme operators

"""

def equalArrays(initial, goal):
    for i in range(len(initial)):
        for j in range(len(initial)):
            if initial[i][j] != goal[i][j]:
                return False
    return True

def misplaced(initial, goal):
    numMis = 0
    size = len(goal)*len(goal)
    for num in range(1, size):
        for i in range(len(initial)):
            for j in range(len(initial)):
                if initial[i][j] == num:
                    if initial[i][j] != goal[i][j]:
                        numMis +=1
    return numMis

def manDist(initial, goal):
    value = 0
    size = len(goal)*len(goal)
    for i in range(size):
        j = 1
    return value


def findIndexOfZero(initial):

    arr = [0,0]
    for i in range(len(initial)):
        for j in range(len(initial[0])):
            if initial[i][j] == 0:
                arr = [i,j]
                return arr
    return arr

def updateQ(curr, queue, seen):
    arr = findIndexOfZero(curr)
    x = arr[0]
    y = arr[1]
    if (moves.left(curr, x, y)) not in seen:
        seen.add(moves.left(curr, x, y))
        queue.append(moves.left(curr, x, y))
    if  moves.right(curr, x, y) not in seen:
        seen.add(right(curr, x, y))
        queue.append(moves.right(curr, x, y))
    if  moves.up(curr, x, y) not in seen:
        seen.add(up(curr,x,y))
        queue.append(moves.up(curr, x, y))
    if moves.down(curr, x, y) not in seen:
        seen.add(down(curr,x,y))
        queue.append(moves.down(curr, x, y))
    #queue.append(moves.down(curr,x, y))
    return queue


def runAlgo(initial,goal):
    arr = findIndexOfZero(initial)
    x = arr[0]
    y = arr[1]
    #need to use priority queue
    queue = []
    queue.append(initial)
    seen = {}
    while True:
        if len(queue) == 0:
            return False
        curr = queue.pop(0)
        #moves.printState(curr)
        if equalArrays(curr,goal):
            return curr
        queue = updateQ(curr, queue, seen)
        if len(queue)%1000 == 0:
            moves.printState(curr)
            print(len(queue))

def left1(initial, x, y):
    c = [list(row) for row in initial]
    moves.printState(c)
    if y-1 >= 0:
        y = y-1
        temp = c[x][y]
        c[x][y] = 0
        c[x][y+1] = temp
    #printState(initial)
    return c


def test(initial,goal):
    moves.printState(initial)
    arr = findIndexOfZero(initial)
    x = arr[0]
    y = arr[1]
    c = left1(initial, x, y)
    moves.printState(initial)
    moves.printState(c)



def main():
    #input ur list
    #which opition do you want to choose
    #perfomr the thing
    initial = [[1,2,3],
              [7,5,6],
              [4,8,0]]

    test(initial,goal)

    #print(equalArrays(initial, goal))
    #runAlgo(initial,goal)

    """
    moves.printState(goal)
    moves.left(goal, 2, 0)
    moves.right(goal,2,0)
    moves.up(goal,2,1 )
    moves.down(goal,1, 1)
    print("hi")
    """

    mis = misplaced(initial, goal)
    print(mis)

main()
