class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums = [0,1,1,1,0,1,1,0,1]
        ans = []
        for i in range(len(nums)):
            if nums[i] == 0:
                ans.append(i)
        #nums = [1,1,1,0,1,0,1,1,1,0,1,1,1]

        left = 0
        right = 0
        n = len(nums)
        mx = 0
        zero = 0

        while right < n:
            if nums[right] == 0:
                zero += 1

            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            mx = max(mx, right - left )
            right += 1
        if len(ans)==0:
            mx=len(nums)-1
        return(mx)