import heapq,math
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        ans = 0
        
        for i in range(len(nums)):
            heapq.heappush(heap, -(nums[i]))
        
        for i in range(k):
            element = -heapq.heappop(heap)
            ans += element  
            heapq.heappush(heap, -math.ceil(element / 3))
        
        return ans
