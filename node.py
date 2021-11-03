class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
    def getPrev(self):
        return self.prev
    def setPrev(self, obj):
        self.prev = obj
    def getValue(self):
        return self.value
    
