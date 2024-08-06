from exception import Empty
class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self._data = list()
    def __len__(self) -> int:
        return len(self._data)
    
    def is_empty(self) -> bool:
        if len(self._data) == 0:
            return True
        else:
            return False
    def top(self):
        if not self.is_empty():
            return self._data[-1]
        else:
            print('The stack is Empty')
        
    def push(self, elem):
        self._data.append(elem)

    def pop(self):
        if not self.is_empty():
            self._data.pop()
        else:
            print('The stack is Empty')
    
    def display(self):
        print(self._data)
    # You can implement this class however you like