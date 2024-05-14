from collections import defaultdict
from typing import List

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.winning = []
        self.count = defaultdict(int)
        current_leader = -1
        
        for i in range(len(persons)):
            self.count[persons[i]] += 1
            if current_leader == -1 or self.count[persons[i]] >= self.count[current_leader]:
                current_leader = persons[i]
            self.winning.append(current_leader)
    
    def q(self, t: int) -> int:
        low, high = 0, len(self.times) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.times[mid] <= t:
                low = mid + 1
            else:
                high = mid - 1
        return self.winning[high]        
