from typing import List
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                num_parts = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
                ans += num_parts - 1
                nums[i] = nums[i] // num_parts
        return ans
