from avl import AVLTree
from object import Object
from object import Color

class Bin:
    def __init__(self, bin_id, capacity):
        self.container = AVLTree()
        self.bin_id = bin_id
        self.capacity = capacity
        self.store_list =[]

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.container.insert_value(object.ID, None)
        



    def remove_object(self, object_id):
        self.container.delete_value(object_id)
        # Implement logic to remove an object by ID
        

    def ret_list(self):
        return self.store(self.container.root)
    def store(self, root):
        if root == None:
            return []
        else:
            return   self.store(root.left) +[root.key] + self.store(root.right)

        

