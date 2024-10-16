'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure


def comp(c1, c2):
    return c1.counter < c2.counter

def comp2(t1,t2):
    if t1[0] + t1[1].arrival_time != t2[0] + t2[1].arrival_time:
        return t1[0] + t1[1].arrival_time < t2[0] + t2[1].arrival_time
    else:
        return t1[1].id < t2[1].id



    
class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        self.crew = heap.Heap(comp, [])
        self.nonzeroelem = []
        
        
        for i in range(m):
            self.crew.insert(crewmate.CrewMate())
        
        
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        mincrew = self.crew.extract()
        
        if mincrew.counter > treasure.arrival_time:
            mincrew.counter += treasure.size
            mincrew.treasury.append(treasure)
        else:
            if len(mincrew.treasury) == 0:
                self.nonzeroelem.append(mincrew)
            mincrew.counter = treasure.size + treasure.arrival_time
            mincrew.treasury.append(treasure)

        self.crew.insert(mincrew)


        

    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        treasure_list = []
        for i in self.nonzeroelem:
            completion_heap = heap.Heap(comp2, [])
            t_prev=0

            for j in i.treasury:
                # j= i.treasury[o]
                remaining_size = j.size
                if completion_heap.top() == None:
                    completion_heap.insert([j.size,j])
                    t_prev = j.arrival_time
                else:

                    del_t = j.arrival_time - t_prev

                    while True:
                        tp = completion_heap.extract()
                        if tp == None:
                            break
                        else:

                            if tp[0] > del_t:
                                tp[0] -= del_t
                                completion_heap.insert(tp)
                                break
                            else:
                                del_t -= tp[0]
                                t_prev += tp[0]
                                tp[1].completion_time= t_prev 
                                treasure_list.append(tp[1])
                    t_prev = j.arrival_time
                    completion_heap.insert([remaining_size, j])

            t_end = i.treasury[-1].arrival_time
            # bachi hui heap khali kar rha
            for k in range(len(completion_heap.data)):
                l = completion_heap.extract()
                t_end += l[0]
                l[1].completion_time = t_end
                treasure_list.append(l[1])
    
        treasure_list.sort(key= lambda i: i.id)
        return treasure_list

                
                
            


    
    # You can add more methods if required
    