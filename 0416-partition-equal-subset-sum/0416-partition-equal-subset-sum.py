class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)/2
        n=len(nums)
        @cache
        def solve(index,cursum):
            if index>=n or cursum>target:
                return False
            if cursum==target:
                return True
            return solve(index+1,cursum+nums[index]) or solve(index+1,cursum)       
        return solve(0,0)     