class Node:
    def __init__(self, parent, value):
        self.parent  = parent
        self.right = None
        self.left = None
        self.value = value
        self.height = 1
        
        