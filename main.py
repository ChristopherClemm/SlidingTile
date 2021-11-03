
import moves

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

initial = [[1,2,3],
          [7,5,6],
          [4,8,0]]


"""
nodes = make queue(makenode(inittalstate)
)
loop do
if emoty return false
node = remove front
if problem = goaltest succeds then return nodesnodes = queeung function node expand problme operators

"""

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


def findIndexOfZero(initial, goal):

    arr = [0,0]
    for i in range(len(initial)):
        for j in range(len(initial[0])):
            if initial[i][j] == 0:
                arr = [i,j]
                return arr
    return arr

def runAlgo(initial,goal):
    arr = findIndexOfZero(initial, goal)
    x = arr[0]
    y = arr[1]
    queue = []
    queue.append(initial)


    while !queue.empty():
        curr = queue.pop():

def main():
    #input ur list
    #which opition do you want to choose
    #perfomr the thing

    arr = findIndexOfZero(initial, goal)
    x = arr[0]
    y = arr[1]
    print(x,y)


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
