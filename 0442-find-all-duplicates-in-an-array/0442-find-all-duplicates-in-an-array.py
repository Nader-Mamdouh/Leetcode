from collections import defaultdict
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
            if dic[i]>1:
                ans.append(i)
        return ans        
        