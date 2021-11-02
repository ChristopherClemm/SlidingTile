
import moves

goal = [[1,2,4],
        [4,5,6],
        [7,8,0]]

initial = [[1,2,4],
          [4,5,6],
          [0,8,7]]

"""
nodes = make queue(makenode(inittalstate)
)
loop do
if emoty return false
node = remove front
if problem = goaltest succeds then return nodesnodes = queeung function node expand problme operators

"""
def manDist(initial, goal):
    value = 0
    size = len(goal)*len(goal)
    for i in size:

    return value


def findIndexOfZero(inittalstate, goal):

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
    moves.printState(goal)
    moves.left(goal, 2, 0)
    moves.right(goal,2,0)
    moves.up(goal,2,1 )
    moves.down(goal,1, 1)
    print("hi")

main()
