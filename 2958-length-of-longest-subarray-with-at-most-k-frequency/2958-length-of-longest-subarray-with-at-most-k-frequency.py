class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        #nums = [1, 2, 3, 1, 2, 3, 1, 2]
        #k = 2
        dic = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(nums)):
            dic[nums[right]] += 1
            while dic[nums[right]] > k:
                dic[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return(ans)

        