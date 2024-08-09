from typing import List
class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        ans = float('inf')
        memo = {}
        
        def solve(cur, n):
            nonlocal ans
            if cur == target:
                ans = min(ans, n)
                return n
            if cur > target:
                return float('inf') 
            if (cur, n) in memo:
                return memo[(cur, n)]
            
            min_coins = float('inf')
            for i in coins:
                min_coins = min(min_coins, solve(cur + i, n + 1))
                
            memo[(cur, n)] = min_coins
            return min_coins
        
        result = solve(0, 0)
        return ans if ans != float('inf') else -1
