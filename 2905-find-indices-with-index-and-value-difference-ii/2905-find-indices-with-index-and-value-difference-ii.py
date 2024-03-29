class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        n = len(nums)
        
        for left in range(n):
            for right in range(left + indexDifference, n):
                if abs(nums[left] - nums[right]) >= valueDifference:
                    return [left, right]
        
        return [-1, -1]
