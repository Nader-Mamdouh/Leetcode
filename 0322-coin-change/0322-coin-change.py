from typing import List

class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        # Initialize the answer to infinity
        ans = float('inf')
        
        # Memoization dictionary to store results of subproblems
        memo = {}
        
        def solve(cur):
            # Base case: if current amount reached the target, return 0 coins
            if cur == target:
                return 0
            # If current amount exceeds the target, return infinity
            if cur > target:
                return float('inf')
            # If the result is already computed, return it from memo
            if cur in memo:
                return memo[cur]
            
            # Initialize minimum coins needed to infinity
            min_coins = float('inf')
            # Iterate through each coin and recursively calculate minimum coins
            for coin in coins:
                # Recursively find minimum coins for current amount + coin value
                result = solve(cur + coin)
                # Update minimum coins if result is valid (not infinity)
                if result != float('inf'):
                    min_coins = min(min_coins, 1 + result)
            
            # Memoize the result for current amount
            memo[cur] = min_coins
            return min_coins
        
        # Start recursive function from amount 0
        result = solve(0)
        
        # Return the answer or -1 if no valid combination found
        return result if result != float('inf') else -1
