from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[-1]*n
        def dfs(index):
            if index>=n:
                return 0
            if memo[index]!=-1:
                return memo[index]
            length=1
            for i in range(index+1,n):
                if nums[i]>nums[index]:
                    length=max(length,1+dfs(i))
            memo[index]=length
            return length        

        max_l=1
        for i in range(n):
            max_l=max(max_l,dfs(i))
        return max_l                