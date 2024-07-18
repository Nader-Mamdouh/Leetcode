from collections import defaultdict
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #nums = [1,3,4,2,2]
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
            if dic[i]>1:
                return i
        