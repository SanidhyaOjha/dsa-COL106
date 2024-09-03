class QueueArray:
    DEFAULT_CAPACITY =10

    def __init__(self) -> None:
        self._data = [None] * QueueArray.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            print("none")
        else:
            return self._data[self._front]
        
    def dequeue(self):
        if self.is_empty():
            print("none")
        else:
            answer = self.first()
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
            self._size -=1

            return answer
        
    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        else:
            self._data[(self._front + self._size)% len(self._data)] = element
            self._size +=1
        
    def resize(self):
        
