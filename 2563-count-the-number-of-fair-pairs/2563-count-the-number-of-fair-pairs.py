from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] >= lower:
                    right = mid - 1
                else:
                    left = mid + 1
            start = left
            left, right = i + 1, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] <= upper:
                    left = mid + 1
                else:
                    right = mid - 1
            end = right
            if start <= end:
                result += end - start + 1

        return result
