'''
Python Code to implement a heap with general comparison function
'''

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
        self.comp=comparison_function
        m=len(init_array)
        self.heap=[]
        for i in range(m):
            self.insert(init_array[i])
        # self.heap=self.build(init_array)
        
        
        # Write your code here
        pass
        
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
        self.heap.append(value)
        j=len(self.heap)-1
        self.upheap(j)
        # pass
    
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
        mval=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()

        self.downheap(0)
        return mval
        pass
    
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
        return self.heap[0]
        
        # Write your code here
        pass
    # def add(self,val):
    #     self.heap.append(val)
    #     j=len(self.heap)-1
    #     self.upheap(j)
    
    # def build(self,arr):
    #     return self.heapify(0,arr)
    
    def upheap(self,indx):
        if(indx<=0):
            return
        pindx=(indx-1)//2
        if(pindx>=0):
            if(not self.comp(self.heap[pindx],self.heap[indx])):
                self.heap[pindx],self.heap[indx]=self.heap[indx],self.heap[pindx]
                self.upheap(pindx)
       
    def downheap(self,indx):
        lchild=2*indx+1
        n=len(self.heap)
        if(lchild>=n):
            return
        sm=lchild
        rchild=2*indx+2
        if(rchild<n):
            if(self.comp(self.heap[rchild],self.heap[lchild])):
                sm=rchild
        if(self.comp(self.heap[sm],self.heap[indx])):
            self.heap[sm],self.heap[indx]=self.heap[indx],self.heap[sm]
            self.downheap(sm)

    # You can add more functions if you want to