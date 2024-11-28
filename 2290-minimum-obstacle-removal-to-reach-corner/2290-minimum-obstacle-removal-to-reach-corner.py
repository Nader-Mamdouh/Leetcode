class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q=deque()
        q.appendleft((0, 0))
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            x,y=q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    newDist = distance[x][y] + grid[nx][ny]
                    if newDist < distance[nx][ny]:
                        distance[nx][ny] = newDist
                        if grid[nx][ny] == 0:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        return distance[m-1][n-1]                    