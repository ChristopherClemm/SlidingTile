
import moves
import node
import heapq as hq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

locationForMan = [[0,(2,2)],
    [1, (0,0)],
    [2, (0,1)],
    [3, (0,2)],
    [4, (1,0)],
    [5, (1,1)],
    [6, (1,2)],
    [7, (2,0)],
    [8, (2,1)]]

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
    size = len(initial)
    for i in range(size):
        for j in range(size):

            val = initial[i][j]
            #print("val = ", val , " other stuff  = ",(i - goal[val-1][1][0]) + (j - goal[val-1][1][1]))
            value += (abs(i - goal[val][1][0])) + (abs(j - goal[val][1][1]))
    return value


def findIndexOfZero(initial):
    arr = [0,0]
    for i in range(len(initial)):
        for j in range(len(initial[0])):
            if initial[i][j] == 0:
                arr = [i,j]
                return arr
    return arr

def updateQ(curr, queue, seen, mode):
    arr = findIndexOfZero(curr.getValue())
    x = arr[0]
    y = arr[1]
    moveLeft = moves.left(curr.getValue(), x, y)
    moveLeftTuple = createTuple(moveLeft)
    if moveLeftTuple not in seen:
        val = curr.getDepth()
        seen.add(moveLeftTuple)
        node1 = node.Node(moveLeft,curr.getDepth()+1)
        node1.setPrev(curr)
        if mode == 2:
            val += misplaced(moveLeft, goal)
        if mode == 3:
            val += manDist(moveLeft, locationForMan)
        queue.append((val, node1))
    moveRight = moves.right(curr.getValue(), x, y)
    moveRightTuple = createTuple(moveRight)
    if  moveRightTuple not in seen:
        val = curr.getDepth()
        seen.add(moveRightTuple)
        node2 = node.Node(moveRight, curr.getDepth()+1)
        node2.setPrev(curr)
        if mode == 2:
            val += misplaced(moveRight, goal)
        if mode == 3:
            val += manDist(moveRight, locationForMan)
        queue.append((val, node2))
    moveUp = moves.up(curr.getValue(), x, y)
    moveUpTuple = createTuple(moveUp)
    if  moveUpTuple not in seen:
        val = curr.getDepth()
        seen.add(moveUpTuple)
        node3 = node.Node(moveUp, curr.getDepth()+1)
        node3.setPrev(curr)
        if mode == 2:
            val += misplaced(moveUp, goal)
        if mode == 3:
            val += manDist(moveUp, locationForMan)
        queue.append((val, node3))
    moveDown = moves.down(curr.getValue(), x, y)
    moveDownTuple = createTuple(moveDown)
    if  moveDownTuple not in seen:
        val = curr.getDepth()
        seen.add(moveDownTuple)
        node4 = node.Node(moveDown, curr.getDepth()+1)
        node4.setPrev(curr)
        if mode == 2:
            val += misplaced(moveDown, goal)
        if mode == 3:
            val += manDist(moveDown, locationForMan)
        queue.append((val, node4))
    #queue.append(moves.down(curr,x, y))
    return queue


def runAlgo(initial,goal,mode):
    arr = findIndexOfZero(initial)
    x = arr[0]
    y = arr[1]
    #need to use priority queue
    nodesExpanded = 0
    queue = []
    nodeI = node.Node(initial,0)
    queue.append((0,nodeI))
    hq.heapify(queue)
    seen = {((0,0,0),(0,0,0),(0,0,0))}
    solutionLen = 0
    while True:
        if len(queue) == 0:
            return False
        #print(queue)
        if mode == 2 or mode == 3:
            hq.heapify(queue)
        curr = queue.pop(0)
        curr = curr[1]
        nodesExpanded +=1
        solutionLen +=1
        #moves.printState(curr)
        if equalArrays(curr.getValue(),goal):
            print("Nodes Expanded = ", nodesExpanded)
            return curr
        queue = updateQ(curr, queue, seen, mode)

def createTuple(iniii):
    tup = ()
    for i in range(len(iniii)):
        tup += tuple(iniii[i])
    #print(tup)
    return tup
"""
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
    queue = []
    nodeI = node.Node(initial)
    nodeII = node.Node(goal)
    queue.append((10,nodeI))
    queue.append((20,nodeII))
    hq.heapify(queue)
    print(moves.printState(queue[0][1].getValue()))

    #moves.printState(queue[0][2].getValue())
    seen = {((0,0,0),(0,0,0),(0,0,0))}

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
    """
def welcome():
    initial = [[8,7,1],
              [6,0,2],
              [5,4,3]]
    val = input("Would you like to make or own puzzle?(Y/N)\n")

    if val == "Y":

        myStr = input("Enter in puzzle using a space as a blank between each letter.\nEnter it is from left to right, top to bottom.\nOnly enter valid puzzles, type the blank with a 0\n")

        myArr = list(map(int, myStr.split()))
        print(myArr)
        count = 0
        for i in range(3):
            for j in range(3):
                print(j)
                initial[i][j] = myArr[count]
                count +=1

    algoMode = input("CHOOSE THE MODE:\n Enter in 1 for uniform\nEnter in a 2 for misplaced\nEnter in 3 for manhattan\n")
    return [initial,algoMode]

def main():
    response = welcome()
    #input ur list
    #which opition do you want to choose
    #perfomr the thing
    """
    initial = [[8,2,3],
              [4,5,6],
              [7,1,0]]

              initial = [[8,7,1],
              [6,0,2],
              [5,4,3]]
    #test(initial,goal)
    initial = [[1,2,3],
              [4,0,5],
              [7,8,6]]
    initial = [[1,6,7],
              [5,0,3],
              [4,8,2]]

    initial1 = [[1,6,7],
              [5,3,0],
              [4,8,2]]
    initial2 = [[5,1,3],
              [4,7,6],
              [0,8,2]]
    print("MAN DIST = " , manDist(initial, locationForMan))
    print("MAN DIST 1 = " , manDist(initial1, locationForMan))
    print("MAN DIST 2 = " , manDist(initial2, locationForMan))
    """

    #print(equalArrays(initial, goal))
    ##print(moves.printState(initial))
    initial = response[0]
    mode = response[1]
    finalSol = runAlgo(initial,goal,mode)
    depth = -1
    while finalSol:
        depth+=1
        moves.printState(finalSol.getValue())
        finalSol = finalSol.prev
    print("The depth is = ", depth)




main()
