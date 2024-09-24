from bin import Bin
from avl import AVLTree
from object import Object, Color
from node import Node
from exceptions import NoBinFoundException


class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.object_master = AVLTree()
        self.bin_by_ID = AVLTree()
        self.main = AVLTree()
        
    def greatest_capacity(self,size):
        on_node=self.main.root
        
        while on_node.right!=None:
            on_node=on_node.right
        if on_node.key>=size:
            return on_node
        else:
            return None
    
    def least_cap(self,on_node,size):
        if on_node==None:
            return on_node
        if on_node.key==size:
            return on_node
        if size<on_node.key:
            go_lf=self.least_cap(on_node.left,size)
            if(go_lf==None):
                return on_node
            else:
                return go_lf
        else:
            go_ri=self.least_cap(on_node.right,size)
            return go_ri
        
    def least_capacity(self,size):
        return self.least_cap(self.main.root, size)
    
    def CFA(self, object_id, size, color):
        least_cap_node = self.least_capacity(size)

        if least_cap_node != None:
            if color == Color.BLUE:
                if least_cap_node.key>=size:
                    least_id_node = least_cap_node.value.min_value_node(least_cap_node.value.root)
                    
                    obj = Object(object_id, size, color)
                    obj.binID = least_id_node.key
                    self.object_master.insert_value(object_id, obj)
                    bin_tree = least_id_node.value
                    
                    least_cap_node.value.delete_value(least_id_node.key)
                    if least_cap_node.value.root == None:
                        self.main.delete_value(least_cap_node.key)
                        
                    binsize = bin_tree.capacity
                    binsize -= size
                    bin_tree.add_object(obj)
                    bin_tree.capacity -=size
                    self.bin_by_ID.search_value(least_id_node.key).value -=size
                    least_id_node.value = bin_tree
                    new_cap_node = self.main.search_value(binsize)

                    if new_cap_node != None:
                        new_cap_node.value.insert_value(least_id_node.key, least_id_node.value)
                    else:
                        tr = Node(binsize, None)
                        tr.value = AVLTree()
                        tr.value.insert_value(least_id_node.key, least_id_node.value)
                        self.main.insert_value(binsize, tr.value)
                        
                else:
                    raise NoBinFoundException
            else:
                if least_cap_node.key>=size:
                    max_id_node = least_cap_node.value.max_value_node(least_cap_node.value.root)
                    obj = Object(object_id, size, color)
                    obj.binID = max_id_node.key
                    self.object_master.insert_value(object_id, obj)
                        
                    bin_tree = max_id_node.value

                    least_cap_node.value.delete_value(max_id_node.key)

                    if least_cap_node.value.root == None:
                        self.main.delete_value(least_cap_node.key)

                    binsize = bin_tree.capacity
                    binsize -= size
                    bin_tree.add_object(obj)
                    bin_tree.capacity -=size
                    self.bin_by_ID.search_value(max_id_node.key).value -=size
                    max_id_node.value = bin_tree
                    new_cap_node = self.main.search_value(binsize)

                    if new_cap_node != None:
                        new_cap_node.value.insert_value(max_id_node.key, max_id_node.value)
                    else:
                        tr = Node(binsize, None)
                        tr.value = AVLTree()
                        tr.value.insert_value(max_id_node.key, max_id_node.value)
                        self.main.insert_value(binsize, tr.value)
                        
                else:
                    raise NoBinFoundException
                    
        else:
            raise NoBinFoundException

    

    def LFA(self, object_id, size, color):
        max_cap_node = self.greatest_capacity(size)
        if max_cap_node != None:

            if color == Color.RED:
                if max_cap_node.key>=size:
                    least_id_node2 = max_cap_node.value.min_value_node(max_cap_node.value.root)
                    obj = Object(object_id, size, color)
                    obj.binID = least_id_node2.key
                    self.object_master.insert_value(object_id, obj)
                        
                    bin_tree = least_id_node2.value
                    max_cap_node.value.delete_value(least_id_node2.key)

                    if max_cap_node.value.root == None:
                        self.main.delete_value(max_cap_node.key)

                    binsize = bin_tree.capacity
                    binsize -= size

                    new_cap_node = self.main.search_value(binsize)
                    bin_tree.add_object(obj)
                    bin_tree.capacity -=size
                    self.bin_by_ID.search_value(least_id_node2.key).value -=size
                    least_id_node2.value = bin_tree
                    if new_cap_node != None:
                        new_cap_node.value.insert_value(least_id_node2.key, least_id_node2.value)
                    else:
                        tr = Node(binsize, None)
                        tr.value = AVLTree()
                        tr.value.insert_value(least_id_node2.key, least_id_node2.value)
                        self.main.insert_value(binsize, tr.value)

                        
                else:
                    raise NoBinFoundException
            else:
                if max_cap_node.key>=size:
                    max_id_node2 = max_cap_node.value.max_value_node(max_cap_node.value.root)
                    obj = Object(object_id, size, color)
                    obj.binID = max_id_node2.key
                    self.object_master.insert_value(object_id, obj)

                    
                    bin_tree = max_id_node2.value
                    max_cap_node.value.delete_value(max_id_node2.key)
                    if max_cap_node.value.root == None:
                        self.main.delete_value(max_cap_node.key)

                    binsize = bin_tree.capacity
                    binsize -= size
                    bin_tree.add_object(obj)
                    bin_tree.capacity -=size
                    self.bin_by_ID.search_value(max_id_node2.key).value -=size
                    max_id_node2.value = bin_tree
                    new_cap_node = self.main.search_value(binsize)
                    if new_cap_node != None:
                        new_cap_node.value.insert_value(max_id_node2.key, max_id_node2.value)
                    else:
                        tr = Node(binsize, None)
                        tr.value = AVLTree()
                        tr.value.insert_value(max_id_node2.key, max_id_node2.value)
                        self.main.insert_value(binsize, tr.value)
                    
                    
                    
                else:
                    raise NoBinFoundException
        else:
            raise NoBinFoundException



        


    def add_bin(self, bin_id, capacity):
        bin_tobe = Bin(bin_id, capacity)
        self.bin_by_ID.insert_value(bin_id, capacity)
        
        bs = self.main.search_value(capacity)
        if bs != None:
            bs.value.insert_value(bin_id, bin_tobe)
        else:
            tr = AVLTree()
            tr.insert_value(bin_id, bin_tobe)
            self.main.insert_value(capacity, tr)
        

    def add_object(self, object_id, size, color):
        
        
        if color == Color.BLUE or color == Color.YELLOW:
            self.CFA(object_id, size, color)
            
        else:
            self.LFA(object_id, size, color)
                    

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        obj_check= self.object_master.search_value(object_id)
        if obj_check != None:
            objjjj= self.object_master.search_value(object_id).value
            obj_bin = objjjj.binID
        
            obj_bin_in_BID = self.bin_by_ID.search_value(obj_bin)

            bin_cap = self.main.search_value(obj_bin_in_BID.value)
            bin_main = bin_cap.value.search_value(obj_bin).value
            
            bin_main.remove_object(object_id)
            
            
            bin_main.capacity += objjjj.size
            
            bin_cap.value.delete_value(obj_bin)
            

            if bin_cap.value.root == None:
                self.main.delete_value(obj_bin_in_BID.value)
            
            
            obj_bin_in_BID.value += objjjj.size

            new_cap_node = self.main.search_value(obj_bin_in_BID.value)

            if new_cap_node != None:
                new_cap_node.value.insert_value(obj_bin, bin_main)
            else:
                tr = Node(obj_bin_in_BID.value, None)
                tr.value = AVLTree()
                tr.value.insert_value(obj_bin, bin_main)
                self.main.insert_value(obj_bin_in_BID.value, tr.value)
            
            self.object_master.delete_value(object_id)
            
            



    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        bin_obj_cap = self.bin_by_ID.search_value(bin_id).value
        bin_obj_cont = self.main.search_value(bin_obj_cap).value
        binfinal = bin_obj_cont.search_value(bin_id).value
        return (binfinal.capacity, binfinal.ret_list())
    
    

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        obj = self.object_master.search_value(object_id)
        if obj:
            return obj.value.binID
        else:
            print("No object exists")
    
    