import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-value for value in piles]
        heapq.heapify(max_heap)      
        for _ in range(k):
            max_value = -heapq.heappop(max_heap)
            reduced_value = max_value - max_value // 2
            heapq.heappush(max_heap, -reduced_value)
        return -sum(max_heap)