class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        ans=0
        def solve(index,summ):
            if index==len(nums):
                return 1 if summ==target else 0
            if (index,summ) in memo:
                return memo[(index,summ)]
            memo[(index,summ)]=solve(index+1,summ+nums[index])+solve(index+1,summ-nums[index])
            return memo[(index,summ)]

        return solve(0,0)