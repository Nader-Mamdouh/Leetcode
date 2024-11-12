from typing import List
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])
        def bs(number):
            left, right = 0, len(items) - 1
            while left <= right:
                mid = (left + right) // 2
                if items[mid][0] <= number:
                    left = mid + 1
                else:
                    right = mid - 1
            return items[right][1] if right >= 0 else 0
        
        ans = []
        for i in queries:
            ans.append(bs(i))
        
        return ans
    