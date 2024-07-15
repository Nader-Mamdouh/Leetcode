from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        q = deque()
        visited = set()
        minute = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))      
        while q:
            size = len(q)
            for n in range(size):
                i, j = q.popleft()
                
                for direction in directions:
                    nx,ny = i + direction[0], j + direction[1]   
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        grid[nx][ny] = 2  
                        q.append((nx, ny))
                        visited.add((nx, ny))       
            if q:
                minute += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return minute
