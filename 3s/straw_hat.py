'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
from custom import Treasure1
def comp_id(treasure1,treasure2):
    return treasure1.id<treasure2.id
def comp(CrewMate1,CrewMate2):
    # if(CrewMate1.load==CrewMate2.load):
    #     return CrewMate1.id<CrewMate2.id
    return (CrewMate1.load+CrewMate1.start_time)<(CrewMate2.load+CrewMate2.start_time)
def compT(treasure1,treasure2):
    p1=(treasure1.arrival_time+treasure1.size)
    p2=(treasure2.arrival_time+treasure2.size)
    if(p1==p2):
        return treasure1.id<treasure2.id
    else:
        return p1<p2

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
        arr=[]
        for i in range(m):
            crew_mate=CrewMate(i)
            arr.append(crew_mate)
        # self.empty_crewmates=arr
        self.loaded_crewmates=[]
        self.crewmates=Heap(comp,arr)
        # Write your code here
        pass
    
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
        # arr=self.crewmates
        crew=self.crewmates.extract()
    
        end=treasure.arrival_time
        a1=1
        if(crew.load==0):
            crew.load=treasure.size
            crew.start_time=end
            self.loaded_crewmates.append(crew)
            a1=0

        if(a1==1 and end>=crew.load+crew.start_time):
            crew.load=treasure.size
            crew.start_time=end
        elif(a1 and end<crew.load+crew.start_time):
            crew.load+=treasure.size
        crew.treasure.append(treasure)
        self.crewmates.insert(crew)
        
        
        # for i in range(len(arr.heap)):
        #     print(arr.heap[i].load," hii  ",end=" ")
        # print('done')

        pass
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        arrm=[]
        crews=self.crewmates
        crews1=self.loaded_crewmates
        # print("len",len(crews1))
        # print(crews1[0].treasure)
        ind=0
        while(ind<len(crews1)):
            crew=crews1[ind]
            t11=[]
            for i in range(len(crew.treasure)):
                newt=Treasure1(crew.treasure[i].id,crew.treasure[i].size,crew.treasure[i].arrival_time)
                # newt=crew.treasure[i]
                t11.append(newt)
            ind+=1
            treasures=Heap(compT,[])
            complTime=0
            crew_treasure=treasures.heap
            end1=0
            for i in range(len(t11)):
                treasure=t11[i]
                arr1=[]
                endTime=treasure.arrival_time
                # print(ind,'heyy',complTime)
                if(len(crew_treasure)==0):
                    complTime=treasure.arrival_time
                    # print('hiii',treasure.id)
                if(len(crew_treasure)>0):
                    # if(complTime!=-1):
                    dt=endTime-complTime

                    # else:
                    #     complTime=crew_treasure[0].arrival_time
                    #     dt=endTime-crew_treasure[0].arrival_time
                    # print("dt:",dt)
                    y=1
                    while(y and dt>0 and len(crew_treasure)>0):
                        topt=treasures.top()
                        if(dt>=topt.size):
                            dt-=topt.size
                            t1=treasures.extract()
                            t1.completion_time=endTime-dt
                            # print(ind,t1.size,t1.id,t1.completion_time)
                            # if(t1.completion_time<t1.size+t1.arrival_time):
                            #     print('hee')
                            complTime=t1.completion_time
                            x=Treasure(t1.id,t1.orignal_size,t1.arrival_time)
                            x.completion_time=t1.completion_time
                            arrm.append(x)
                        else:
                            y=0
                            break
                    if(not y and len(crew_treasure)>0):
                        t1=treasures.extract()
                        t1.size-=dt
                        treasures.insert(t1)
                        complTime=endTime
                        # print(ind,'goooo',dt)
                # else:
                #     complTime=endTime
                #     end1=endTime

                if(len(crew_treasure)==0):
                    complTime=endTime
                    # end1=endTime
                treasures.insert(treasure)
                
                
            # if(complTime==-1 and len(crew_treasure)>0):
            #     complTime=crew_treasure[0].arrival_time

            while(len(crew_treasure)>0):
                t1=treasures.extract()
                t1.completion_time=complTime+t1.size
                # print('hello!',complTime,t1.size)
                # if(t1.completion_time<t1.size):
                #     print('hee1')
                x=Treasure(t1.id,t1.orignal_size,t1.arrival_time)
                x.completion_time=t1.completion_time
                arrm.append(x)
                complTime=t1.completion_time


        # for j in range(len(arrm)):
        #     print(arrm[j].id,"hiii")

        newHeap=Heap(comp_id,arrm)
        hp=newHeap.heap
        a1=[]
        # print(hp[0].id)
        while(len(newHeap.heap)>0):
            r=newHeap.extract()
            a1.append(r)
        return a1
        # pass

    
    # You can add more methods if required
