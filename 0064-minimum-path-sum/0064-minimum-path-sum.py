from typing import List, Tuple

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==j==0:
                    continue
                up=down=float('inf')
                if i !=0:
                    up=grid[i][j]+grid[i-1][j]
                if j !=0:
                    down=grid[i][j]+grid[i][j-1]   
                grid[i][j]=min(up,down)
        return grid[n-1][m-1]             
