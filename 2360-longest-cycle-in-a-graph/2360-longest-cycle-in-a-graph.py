from typing import List
from collections import defaultdict

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        white = 0  # unvisited nodes
        grey = 1   # nodes being visited (in the current DFS path)
        black = 2  # fully visited nodes
        max_cycle_len = -1  # to track the longest cycle found
        
        # Track visit states of each node (white: unvisited, grey: visiting, black: visited)
        visit_state = [white] * len(edges)
        # Track the depth of each node in the current DFS path to compute cycle length
        depth_map = {}
        
        def dfs(node: int, current_depth: int) -> int:
            nonlocal max_cycle_len
            if node == -1:  # if the node has no outgoing edge, return
                return -1
            
            if visit_state[node] == black:  # Node already fully processed
                return -1
            
            if visit_state[node] == grey:  # Cycle detected, calculate cycle length
                return current_depth - depth_map[node]  # Cycle length is current depth minus depth when node was first visited
            
            # Mark the node as grey (being visited) and set its depth in the path
            visit_state[node] = grey
            depth_map[node] = current_depth
            
            # Visit the next node in the edges list
            next_node = edges[node]
            cycle_len = dfs(next_node, current_depth + 1)
            
            # After DFS, mark the node as fully visited (black)
            visit_state[node] = black
            return cycle_len
        
        # Explore each node using DFS
        for i in range(len(edges)):
            if visit_state[i] == white:  # Only start a DFS if the node hasn't been visited
                cycle_len = dfs(i, 0)
                if cycle_len > max_cycle_len:
                    max_cycle_len = cycle_len
        
        return max_cycle_len
