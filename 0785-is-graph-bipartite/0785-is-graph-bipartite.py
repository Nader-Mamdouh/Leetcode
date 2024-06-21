from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n  
        ans = True      
        def dfs(node, color):
            nonlocal ans
            colors[node] = color     
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    #print(neighbor)
                    #print(color)
                    ans = False
                elif colors[neighbor] == -1:
                    dfs(neighbor, 1 - color)      
        for i in range(n):
            if colors[i] == -1:
                dfs(i, 0)
                if not ans:
                    return False
        
        return True
