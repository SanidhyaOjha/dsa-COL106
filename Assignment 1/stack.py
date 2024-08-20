class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.data = list()
    # You can implement this class however you like
    def __len__(self) -> int:
        return len(self.data)
    
    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        else:
            return False
    def top(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            print('The stack is Empty')
        
    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if not self.is_empty():
            self.data.pop()
        else:
            print('The stack is Empty')
    
    def display(self):
        print(self.data)
    