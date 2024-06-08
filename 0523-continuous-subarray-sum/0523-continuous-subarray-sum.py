from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix_mod = {0: -1}
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if k != 0:
                prefix_sum %= k
            
            if prefix_sum in prefix_mod:
                if i - prefix_mod[prefix_sum] > 1:
                    return True
            else:
                prefix_mod[prefix_sum] = i
        
        return False
