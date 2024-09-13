from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        dic = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                dic[stop].append(i)

        qsource = deque([(source, 0)]) 
        visited_stops = set([source])  
        visited_buses = set()  
        
        while qsource:
            current_stop, buses_taken = qsource.popleft()
            for bus in dic[current_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for stop in routes[bus]:
                    if stop == target:
                        return buses_taken + 1  
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        qsource.append((stop, buses_taken + 1))
        return -1
