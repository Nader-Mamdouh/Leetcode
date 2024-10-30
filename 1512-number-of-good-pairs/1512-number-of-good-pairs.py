class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        dic =defaultdict(int)
        ans=0
        for i in range(len(nums)):
            dic[nums[i]]+=1
        for i ,num in enumerate(nums):
            dic[num]-=1
            ans+=dic[num]
        return ans        