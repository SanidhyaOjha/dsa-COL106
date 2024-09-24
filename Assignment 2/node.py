
class Node:
    def __init__(self, key, value):
        # self.parent  = parent
        self.key = key
        self.right = None
        self.left = None
        self.value = value
        self.height = 1
        
    