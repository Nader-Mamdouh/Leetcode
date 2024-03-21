class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target in nums:
            return 1
        sm=sum(nums)
        if target>sm:
            return 0

        left = 0
        right = 0
        n = len(nums)
        result = float('inf')  
        ans = nums[left]  

        while left < n and right < n:
            if ans < target:
                right += 1
                if right < n:
                    ans += nums[right]
            else:
                result = min(result, right - left + 1)
                ans -= nums[left]
                left += 1

                while left <= right and ans >= target:
                    result = min(result, right - left + 1)
                    ans -= nums[left]
                    left += 1
        return result

        