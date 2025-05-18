class Queue:
    DEFAULT_CAP = 25
    def __init__(self):
        self.data =[None]*Queue.DEFAULT_CAP
        self.size =0
        self.fr = 0
        
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def first(self):
        if self.is_empty():
            return None
        return self.data[self.fr]
    def enqueue(self, e):
        if self.size== len(self.data):
            self.resize(2*len(self.data))
        slot = (self.fr + self.size)% len(self.data)
        self.data[slot] =e
        self.size +=1
    def dequeue(self):
        if self.is_empty():
            return None
        ans = self.data[self.fr]
        self.data[self.fr] = None
        self.fr = (self.fr +1) % len(self.data)
        self.size -=1
        return ans
    def resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self.fr
        for k in range(self.size):
            self.data[k]=old[walk]
            walk=(1+walk)%len(old)
        self.fr = 0
    