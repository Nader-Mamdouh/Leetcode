from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)     
        for s in strs:
            sorted_str = ''.join(sorted(s))
            dic[sorted_str].append(s)
        ans = list(dic.values())
        
        return ans
