from typing import List, Tuple

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = {}       
        def solve(i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            
            if (i, j) in memo:
                return memo[(i, j)]
            down_sum = solve(i + 1, j) if i + 1 < n else float('inf')
            right_sum = solve(i, j + 1) if j + 1 < m else float('inf')
            memo[(i, j)] = grid[i][j] + min(down_sum, right_sum)       
            return memo[(i, j)]
        
        return solve(0, 0)
