from heapq import *
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        leftheap = []
        rightheap = []
        ans = 0
        l, r = 0, len(costs) - 1
        while l < n and len(leftheap) < candidates:
            heappush(leftheap, costs[l])
            l += 1
        while r >=l and len(rightheap) < candidates:
            heappush(rightheap, costs[r])
            r -= 1
        while k > 0:
            if leftheap and rightheap:
                if leftheap[0] <= rightheap[0]:
                    ans += heappop(leftheap)
                    if l <= r:
                        heappush(leftheap, costs[l])
                        l += 1
                else:
                    ans += heappop(rightheap)
                    if l <= r:
                        heappush(rightheap, costs[r])
                        r -= 1
            elif leftheap:
                ans += heappop(leftheap)
                if l <= r:
                    heappush(leftheap, costs[l])
                    l += 1
            elif rightheap:
                ans += heappop(rightheap)
                if l <= r:
                    heappush(rightheap, costs[r])
                    r -= 1
            k -= 1
        return ans