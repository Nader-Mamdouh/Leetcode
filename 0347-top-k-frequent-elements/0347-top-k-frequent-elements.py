import heapq
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        max_heap = [[-value, key] for key, value in dic.items()]
        heapq.heapify(max_heap)
        ans = []
        for _ in range(k):
            max_value, digit = heapq.heappop(max_heap)
            ans.append(digit)
        
        return ans
