from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def build_directed_graph(n):
            graph = {i: [] for i in range(n)}
            for i in range(n - 1):
                graph[i].append((i + 1, 1))  
            return graph
        
        def add_adj(left, right, directed_graph):
            directed_graph[left].append((right, 1)) 
            return directed_graph
        
        def bfs(directed_graph):
            visited = set()
            queue = deque([(0, 0)])  # (node, distance)
            distances = {i: float('inf') for i in range(n)}
            distances[0] = 0

            while queue:
                current_node, current_dist = queue.popleft()
                if current_node in visited:
                    continue
                visited.add(current_node)

                for neighbor, weight in directed_graph[current_node]:
                    if current_dist + weight < distances[neighbor]:
                        distances[neighbor] = current_dist + weight
                        queue.append((neighbor, current_dist + weight))
            
            return distances
        directed_graph = build_directed_graph(n)
        result = []
        for left, right in queries:
            directed_graph = add_adj(left, right, directed_graph)
            distances = bfs(directed_graph)
            result.append(distances[n - 1])  
        
        return result
