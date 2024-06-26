from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        
        while left < right:
            mid = (left + right) // 2
            if citations[mid] == len(citations) - mid:
                return len(citations) - mid
            elif citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                right = mid
        
        return len(citations) - left
