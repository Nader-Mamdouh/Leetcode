from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        ans = [[float('inf')] * n for _ in range(m)]

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    ans[i][j] = 0

        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if valid(x, y) and ans[x][y] >= ans[i][j] + 1:
                    ans[x][y] = ans[i][j] + 1
                    q.append((x, y))

        return ans
