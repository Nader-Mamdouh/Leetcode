from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n
        def union(u,v):
            root_u = find(u)
            root_v = find(v)           
            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                elif rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])  
            return parent[u]

        for u, v, score in roads:
            union(u - 1, v - 1) 

        min_score = float('inf')
        for u, v, score in roads:
            if find(0) == find(u - 1):  
                min_score = min(min_score, score)
        
        return min_score        
