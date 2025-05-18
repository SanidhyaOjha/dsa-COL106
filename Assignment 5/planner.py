from flight import Flight

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
    

def comparison_function(a1,a2):
    return a1[0]<a2[0]

def comparison_function2(a1,a2):
    if a1[0] == a2[0]:
        return a1[1] < a2[1]
    return a1[0]<a2[0]

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
       
        self.comp = comparison_function
        self.data = init_array

        if len(self.data)>1:
            self.heapify()

    def insert(self, value):
        self.data.append(value)
        self.upheap(len(self.data)-1)
    
    def extract(self):
        if self.is_empty():
            return None
        self.swap(0, len(self.data)-1)
        item = self.data.pop()
        self.downheap(0)
        return item
    
    def top(self):
        if self.is_empty():
            return None
        return self.data[0]
    

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

class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.flights = flights
        self.no_of_cities = 0
        for f in flights:
            self.no_of_cities = max(self.no_of_cities, f.start_city, f.end_city)
        self.no_of_cities +=1
        # each city stores flights that fly from it as start city
        self.inlist = [[] for i in range(self.no_of_cities)]
        for f in flights:
            self.inlist[f.start_city].append(f)
        # print()
        

            
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        if start_city == end_city:
            return []
        optimal = [float('inf'), float('inf'), None]
        visited = [False]*len(self.flights)
        path = [None]*len(self.flights)
        qu = Queue()
       
        for j in range(len(self.inlist[start_city])):
            f = self.inlist[start_city][j]
            if f.departure_time >= t1 and f.arrival_time <=t2:
                qu.enqueue([0,f.arrival_time, f.end_city, f])
                visited[f.flight_no] = True
        
        while not qu.is_empty():
            pr_flight = qu.dequeue()
            # visited[curr[-1].flight_no] = True
            if pr_flight[2] == end_city:
                if (pr_flight[0] < optimal[0]) or (pr_flight[0] == optimal[0] and pr_flight[1] < optimal[1]):
                    optimal = [pr_flight[0], pr_flight[1], pr_flight[3]]
            else:
                for fe in self.inlist[pr_flight[2]]:
                    if not visited[fe.flight_no] and fe.departure_time >= (pr_flight[1]+20) and fe.arrival_time <=t2:
                        qu.enqueue([pr_flight[0]+1, fe.arrival_time, fe.end_city, fe])
                        path[fe.flight_no] = pr_flight[3]
                        visited[fe.flight_no] = True
        
        if optimal[-1] == None:
            return []
        return self.path_tracker(optimal, path)
        
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        if start_city == end_city:
            return []
        
        pq = Heap(comparison_function,[])
        optimal = [float('inf'), None]
        visited = [False]*len(self.flights)
        path = [None]*len(self.flights)

        for j in range(len(self.inlist[start_city])):
            f = self.inlist[start_city][j]
            if f.departure_time >= t1 and f.arrival_time <=t2:
                # print("qualified")
                pq.insert([f.fare, f.end_city, f])
                visited[f.flight_no] =True

        # print(pq.data)
        while not pq.is_empty():
            pr_flight = pq.extract()
            # visited[curr[-1].flight_no] =True
            if pr_flight[1] == end_city:
                if pr_flight[0] < optimal[0] :
                    optimal = [pr_flight[0], pr_flight[2]]
            else:
                for fe in self.inlist[pr_flight[1]]:
                    if not visited[fe.flight_no] and fe.departure_time>=( pr_flight[2].arrival_time +20) and fe.arrival_time<=t2:
                        pq.insert([pr_flight[0] + fe.fare, fe.end_city, fe])
                        path[fe.flight_no] = pr_flight[2]
                        visited[fe.flight_no] =True

        
        
        if optimal[-1] == None:
            return []
        
        return self.path_tracker(optimal, path)

    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        
        if start_city == end_city:
            return []
        
        pq = Heap(comparison_function2,[])
        optimal = [float('inf'), float('inf'), None]
        visited = [False]*len(self.flights)
        path = [None]*len(self.flights)

        for j in range(len(self.inlist[start_city])):
            f = self.inlist[start_city][j]
            if f.departure_time >= t1 and f.arrival_time <=t2:
                # print("qualified")
                pq.insert([0,f.fare, f.end_city, f])
                visited[f.flight_no] =True

        # print(pq.data)
        while not pq.is_empty():
            pr_flight = pq.extract()
            # visited[curr[-1].flight_no] =True
            if pr_flight[2] == end_city:
                if pr_flight[0] < optimal[0] or  (pr_flight[0] == optimal[0] and pr_flight[1]< optimal[1]):
                    optimal = [pr_flight[0], pr_flight[1], pr_flight[3]]
                    # print(optimal)
            else:
                for fe in self.inlist[pr_flight[2]]:
                    # print("here")
                    if not visited[fe.flight_no] and fe.departure_time>=( pr_flight[3].arrival_time +20) and fe.arrival_time<=t2:
                        pq.insert([pr_flight[0] +1 , pr_flight[1] + fe.fare, fe.end_city, fe])
                        path[fe.flight_no] = pr_flight[3]
                        visited[fe.flight_no] =True

        if optimal[-1] == None:
            return []
        return self.path_tracker(optimal, path)
        
    
    def path_tracker(self,optimal, path):
        final = [optimal[-1],]
        ind = optimal[-1].flight_no
        while True:
            if path[ind] == None:
                return final[::-1]
            final.append(path[ind])
            ind = path[ind].flight_no