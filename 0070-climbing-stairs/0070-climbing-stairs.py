class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def solve(level):
            if level > n:
                return 0
            if level == n:
                return 1
            if level in memo:
                return memo[level]
            
            ans = 0
            for i in range(1, 3):
                ways = solve(level + i)
                ans += ways
            
            memo[level] = ans
            return ans
        
        return solve(0)
