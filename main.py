
import moves
import node
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
    arr = findIndexOfZero(curr.getValue())
    x = arr[0]
    y = arr[1]
    moveLeft = moves.left(curr.getValue(), x, y)
    moveLeftTuple = createTuple(moveLeft)
    if moveLeftTuple not in seen:
        seen.add(moveLeftTuple)
        node1 = node.Node(moveLeft)
        node1.setPrev(curr)
        queue.append(node1)
    moveRight = moves.right(curr.getValue(), x, y)
    moveRightTuple = createTuple(moveRight)
    if  moveRightTuple not in seen:
        seen.add(moveRightTuple)
        node2 = node.Node(moveRight)
        node2.setPrev(curr)
        queue.append(node2)
    moveUp = moves.up(curr.getValue(), x, y)
    moveUpTuple = createTuple(moveUp)
    if  moveUpTuple not in seen:
        seen.add(moveUpTuple)
        node3 = node.Node(moveUp)
        node3.setPrev(curr)
        queue.append(node3)
    moveDown = moves.down(curr.getValue(), x, y)
    moveDownTuple = createTuple(moveDown)
    if  moveDownTuple not in seen:
        seen.add(moveDownTuple)
        node4 = node.Node(moveDown)
        node4.setPrev(curr)
        queue.append(node4)
    #queue.append(moves.down(curr,x, y))
    return queue


def runAlgo(initial,goal):
    arr = findIndexOfZero(initial)
    x = arr[0]
    y = arr[1]
    #need to use priority queue
    queue = []
    nodeI = node.Node(initial)
    queue.append(nodeI)
    seen = {((0,0,0),(0,0,0),(0,0,0))}
    solutionLen = 0
    while True:
        if len(queue) == 0:
            return False
        curr = queue[0]
        solutionLen +=1
        #moves.printState(curr)
        if equalArrays(curr.getValue(),goal):
            return curr
        queue = updateQ(curr, queue, seen)
        if misplaced(curr.getValue(), goal) < 2:
            moves.printState(curr.getValue())
        queue.pop(0)
        if len(queue)%1000 == 0:
            #moves.printState(curr)
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

def createTuple(iniii):
    tup = ()
    for i in range(len(iniii)):
        tup += tuple(iniii[i])
    #print(tup)
    return tup

def test(initial,goal):
    moves.printState(initial)
    arr = findIndexOfZero(initial)
    x = arr[0]
    y = arr[1]
    c = left1(initial, x, y)
    moves.printState(initial)
    moves.printState(c)
    seen = {((0,0,0),(0,0,0),(0,0,0))}
    print(type(tuple(c)))
    c = createTuple(c)
    seen.add(tuple(c))


def main():
    #input ur list
    #which opition do you want to choose
    #perfomr the thing
    initial = [[8,7,1],
              [6,0,2],
              [5,4,3]]

    #test(initial,goal)



    #print(equalArrays(initial, goal))
    finalSol = runAlgo(initial,goal)
    while finalSol:
        moves.printState(finalSol.getValue())
        finalSol = finalSol.prev

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
