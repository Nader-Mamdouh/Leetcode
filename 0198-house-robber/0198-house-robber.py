class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo={}
        def solve(index):
            if index>=n:
                return 0
            if index in memo:
                return memo[index]    
            leng=0
            leng=max(leng,nums[index]+solve(index+2) )
            memo[index]=leng
            return leng  
        mx=-1
        for i in range(n):
            mx=max(mx,solve(i) )
        return mx            