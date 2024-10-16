# You can add any additional function and class you want to implement in this file
'''
    Python file to implement the Treasure class
'''

class Treasure1:
    '''
    Class to implement a treasure
    '''
    
    def __init__(self, id, size, arrival_time):
        '''
        Arguments:
            id : int : The id of the treasure (unique positive integer for each treasure)
            size : int : The size of the treasure (positive integer)
            arrival_time : int : The arrival time of the treasure (non-negative integer)
        Returns:
            None
        Description:
            Initializes the treasure
        '''
        
        # DO NOT EDIT THE __init__ method
        self.id = id
        self.orignal_size = size
        self.arrival_time = arrival_time
        self.completion_time = None
        self.size=size
    
    # You can add more methods if required