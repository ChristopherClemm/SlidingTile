class Node:
    #initializes node and sets values
    def __init__(self, value,depth):
        self.value = value
        self.prev = None
        self.depth = depth
        self.man = 0
    #was used in testing
    def setMan(self, man):
        self.man = man
    #used for backtracking
    def getPrev(self):
        return self.prev
    #used for backtracking
    def setPrev(self, obj):
        self.prev = obj
    def getValue(self):
        return self.value
    def getDepth(self):
        return self.depth
    def getMan(self):
        return self.man
    #needed when priority queue has too same values and needed the user to define the pattern for when they are equal to each other
    #when equal to just select the first one. (it doesnt matter which one gets selected in the A* algo)
    def __lt__(self, other):
        return self
