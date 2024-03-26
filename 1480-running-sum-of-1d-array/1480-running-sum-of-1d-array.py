class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        running_sum = 0
        for num in nums:
            running_sum += num
            ans.append(running_sum)
        return ans
