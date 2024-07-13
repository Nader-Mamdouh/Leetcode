from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = -1
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))  
        if len(queue) == 0 or len(queue) == len(grid) * len(grid[0]):
            return -1
        while queue:
            row, col, dist = queue.pop(0)      
            for x, y in direc:
                nx, ny = row + x, col + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                    grid[nx][ny] = dist + 1 
                    ans = max(ans, dist + 1)
                    queue.append((nx, ny, dist + 1))
        
        return ans