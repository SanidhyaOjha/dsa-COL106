'''
    Python file to implement the class CrewMate
'''
import heap

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self,i):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.id=i
        # self.treasure=heap([])
        self.treasure=[]
        self.start_time=0
        self.load=0
        self.remaining_size=0
        pass
    
    # Add more methods if required