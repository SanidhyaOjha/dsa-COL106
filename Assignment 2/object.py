from enum import Enum

class Color(Enum):
    BLUE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4
    

class Object:
    def __init__(self, object_id, size, color):
        self.ID = object_id
        self.binID = None
        self.color =color
        self.size = size
        self.info = [size, color, self.binID]
