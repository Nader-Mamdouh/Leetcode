class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*n
        if n==1:
            return 1
        if n==2:
            return 2
                
        dp[0]=1
        dp[1]=2
        for i in range(n):
            dp[i]+=dp[i-1]
        return dp[-1]    
