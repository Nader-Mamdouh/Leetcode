from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(int)
        dic2 = defaultdict(int)
        for i in nums1:
            dic[i] += 1
        for i in nums2:
            dic2[i] += 1  
        
        ans = []
        for key in dic:
            if key in dic2:
                for _ in range(min(dic[key], dic2[key])):
                    ans.append(key)
                    
        return ans
