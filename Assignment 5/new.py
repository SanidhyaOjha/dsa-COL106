from flight import Flight
from planner import Planner

flights = [Flight(0, 0, 0, 1, 30, 50),      # City 0 to 1
               Flight(1, 1, 50, 2, 80, 200),     # City 0 to 3
               
               Flight(2, 1, 50, 2, 60, 20),     # City 1 to 2
            #    Flight(3, 1, 50, 2, 100, 120),   # City 1 to 2
               
            #    Flight(4, 2, 120, 4, 200, 100),  # City 2 to 4
               
            #    Flight(5, 3, 100, 4, 150, 500),  # City 3 to 4
            #    Flight(6, 3, 100, 4, 250, 300)   # City 3 to 4
               ]
    
flight_planner = Planner(flights)

route2 = flight_planner.least_flights_earliest_route(0, 2, 0, 100)
print([r.flight_no for r in route2])

# Expected : [0, 2]