from typing import List
from collections import defaultdict

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        end = []
        start = []
        for i in range(len(intervals)):
            dic[intervals[i][0]] = i
            end.append((intervals[i][1], i))
            start.append(intervals[i][0])
        
        start.sort()
        result = [-1] * len(intervals)
        
        for en, idx in end:
            low = 0
            high = len(start) - 1
            while low < high:
                mid = (low + high) // 2
                if start[mid] >= en:
                    high = mid
                else:
                    low = mid + 1
            
            if start[low] >= en:
                result[idx] = dic[start[low]]
        
        return result
