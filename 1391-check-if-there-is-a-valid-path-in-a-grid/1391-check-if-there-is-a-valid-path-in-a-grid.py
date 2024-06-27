from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        def in_bounds(row, col):
            return 0 <= row < n and 0 <= col < m
        
        def dfs(row, col):
            if not in_bounds(row, col):
                return False
            if (row, col) == (n - 1, m - 1):
                return True
            if (row, col) in visited:
                return False
            
            visited.add((row, col))
            street = grid[row][col]
            
            for dr, dc, valid_streets in directions[street]:
                new_row, new_col = row + dr, col + dc
                if in_bounds(new_row, new_col) and grid[new_row][new_col] in valid_streets:
                    if dfs(new_row, new_col):
                        return True
            
            visited.remove((row, col))
            return False
        
        directions = {
            1: [(0, 1, [1, 3, 5]), (0, -1, [1, 4, 6])], # right, left
            2: [(1, 0, [2, 5, 6]), (-1, 0, [2, 3, 4])], # down, up
            3: [(0, -1, [1, 4, 6]), (1, 0, [2, 5, 6])], # left, down
            4: [(0, 1, [1, 3, 5]), (1, 0, [2, 5, 6])],  # right, down
            5: [(0, -1, [1, 4, 6]), (-1, 0, [2, 3, 4])], # left, up
            6: [(0, 1, [1, 3, 5]), (-1, 0, [2, 3, 4])]  # right, up
        }
        
        visited = set()
        return dfs(0, 0)
