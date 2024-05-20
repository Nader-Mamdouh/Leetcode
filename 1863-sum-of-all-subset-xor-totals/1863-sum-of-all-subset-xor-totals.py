from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_xor = 0
        for num in nums:
            total_xor |= num  
        subset_count = 1 << (len(nums) - 1)  
        return total_xor * subset_count
