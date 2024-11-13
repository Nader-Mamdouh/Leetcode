from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(city):
            if city != parent[city]:
                parent[city] = find(parent[city])  
            return parent[city]

        def union(city1, city2):
            root1 = find(city1)
            root2 = find(city2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return len(set(find(i) for i in range(n)))
