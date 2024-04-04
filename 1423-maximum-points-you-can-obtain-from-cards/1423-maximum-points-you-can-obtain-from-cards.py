class Solution(object):
    def maxScore(self, nums, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        if k==n:
            return sum(nums)
        prefix = []
        suffix = []
        cursum=0

        for i in range(1, n):
            cursum+=nums[i-1]
            prefix.append(cursum)
        cursum=0

        for i in range(n-2, -1, -1):
            cursum += nums[i + 1]
            suffix.append(cursum)
        return(max(prefix[k-1],suffix[k-1]))


        
