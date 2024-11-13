from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        
        for i in range(n - 1):
            lb = bisect_left(nums, lower - nums[i], i + 1)
            ub = bisect_right(nums, upper - nums[i], i + 1)
            ans += (ub - lb)
            
        return ans
