from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}

        def solve(i, j):
           
            if i == n - 1:
                return matrix[i][j]
            
            if (i, j) in memo:
                return memo[(i, j)]
          
            down_sum = solve(i + 1, j) if i + 1 < n else float('inf')
            down_left_sum = solve(i + 1, j - 1) if i + 1 < n and j - 1 >= 0 else float('inf')
            down_right_sum = solve(i + 1, j + 1) if i + 1 < n and j + 1 < len(matrix[i]) else float('inf')
            
            memo[(i, j)] = matrix[i][j] + min(down_sum, down_left_sum, down_right_sum)
            return memo[(i, j)]
        
        min_path_sum = float('inf')
        for j in range(len(matrix[0])):
            min_path_sum = min(min_path_sum, solve(0, j))
        
        return min_path_sum
