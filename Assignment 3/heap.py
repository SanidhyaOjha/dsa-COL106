'''
Python Code to implement a heap with general comparison function
'''
from custom import Empty
def comparison_function(a1,a2):
    return a1<a2

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.comp = comparison_function
        self.data = init_array

        if len(self.data)>1:
            self.heapify()

        

        
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.data.append(value)
        self.upheap(len(self.data)-1)
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.is_empty():
            return None
        self.swap(0, len(self.data)-1)
        item = self.data.pop()
        self.downheap(0)
        return item
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.is_empty():
            return None
        return self.data[0]
    
    # You can add more functions if you want to
    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False
    
    def heapify(self):
        initial = self.parent(len(self.data)-1)
        for j in range(initial, -1,-1):
            self.downheap(j)

        
    def upheap(self,index):
        par = self.parent(index)
        if index>0 and self.comp(self.data[index], self.data[par]):
            self.swap(index, par)
            self.upheap(par)

    def downheap(self, index):
        if self.has_left(index):
            left = self.left(index)
            tar = left
            if self.has_right(index):
                right = self.right(index)
                if self.comp(self.data[right], self.data[left]):
                    tar = right
            if self.comp(self.data[tar], self.data[index]):
                self.swap(tar, index)
                self.downheap(tar)

    def right(self, index):
        return 2*index +2

    def left(self, index):
        return 2*index +1
    
    def parent(self, index):
        return (index-1)//2
    
    def has_left(self, index):
        return self.left(index) < len(self.data)
    
    def has_right(self, index):
        return self.right(index) < len(self.data)
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

if __name__ == "__main__":
    hp = Heap(comparison_function, [])
    hp.insert(10)
    hp.insert(20)
    hp.insert(30)
    hp.insert(100)
    hp.insert(5)
    hp.insert(25)
    print(hp.extract())
    print(hp.extract())
    print(hp.top())
    hp.insert(70)
    hp.insert(4)
    print(hp.extract())
    print(hp.extract())
    hp.insert(1)
    print(hp.top())
    hp.insert(-100)
    print(hp.top())
    print(hp.data)