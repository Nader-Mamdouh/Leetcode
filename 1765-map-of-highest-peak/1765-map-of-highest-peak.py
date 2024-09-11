from collections import deque
from typing import List
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(isWater)
        m = len(isWater[0])
        ans = [[-1 for j in range(m)] for i in range(n)]
        q = deque()   
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    ans[i][j] = 0  
                    q.append((i, j))  
        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < n and 0 <= new_j < m and ans[new_i][new_j] == -1:
                    ans[new_i][new_j] = ans[i][j] + 1  
                    q.append((new_i, new_j))  

        return ans
