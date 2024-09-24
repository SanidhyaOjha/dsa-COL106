from node import Node
   
def comp_2(key_1, key_2):
    return key_1 - key_2

    

class AVLTree:
    def __init__(self, compare_function=comp_2):
        self.root = None
        self.size = 0
        self.comp = compare_function

    def height(self,node):
        if not node:
            return 0
        return node.height
    

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    
    
    def insert(self, root, key, value):
        newNode = Node(key, value)
        if not root:
            if self.root == None:
                self.root = newNode
            return newNode
        
        elif self.comp(key,root.key) < 0:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        root.height = 1 + max(self.height(root.left) , self.height(root.right))
        balance = self.balance(root)

        if balance> 1 and key < root.left.key:
            return self.right_rotate(root)
        
        if balance< -1 and key > root.right.key:
            return self.left_rotate(root)
        
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    

    def delete(self, root, key):
        if root is None:
            return None

        if self.comp(key,root.key) < 0:
            root.left = self.delete(root.left, key)
        elif self.comp(key,root.key) > 0:
            root.right = self.delete(root.right,key)
        else:
            if(not root.left):
                t=root.right
                root=None
                return t
            elif(not root.right):
                t=root.left
                root=None
                return t
            else:

                temp = self.min_value_node(root.right)
                root.key = temp.key
                root.value = temp.value
                root.right = self.delete(root.right, temp.key)

        if root is None:
            return None

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self,root):
        current = root
        while current.left != None:
            current = current.left
        return current
    
    def max_value_node(self,root):
        current = root
        while current.right != None:
            current = current.right
        return current

    def search(self, root, key):
        if not root :
            return None
        if self.comp(key,root.key) == 0:
            return root
        if self.comp(key,root.key) > 0:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def insert_value(self, key, value):
        self.root = self.insert(self.root,key,  value)

    def delete_value(self, key):
        self.root = self.delete(self.root,key)

    def search_value(self, key):
        return self.search(self.root, key)
    def ret_root(self):
        return self.root.height
    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key)
            
            self.inorder_traversal(root.right)
    
