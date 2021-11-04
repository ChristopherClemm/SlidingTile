class Node:
    def __init__(self, value,depth):
        self.value = value
        self.prev = None
        self.depth = depth
    def getPrev(self):
        return self.prev
    def setPrev(self, obj):
        self.prev = obj
    def getValue(self):
        return self.value
    def getDepth(self):
        return self.depth
    #NEEDED WHEN WEIGHTS ARE THE SAME
    def __lt__(self, other):
        return self
