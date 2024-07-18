class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list = []
        for i in range(len(nums) + 1):
            list.append(i)

        for i in list: 
            if i not in nums:
                return(i)
           
        