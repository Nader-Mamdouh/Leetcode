from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs_tree(root):
            if root is None:
                return []
            queue = deque([root])
            levels = []
            while queue:
                level_size = len(queue)
                current_level = []
                for _ in range(level_size):
                    current_node = queue.popleft() 
                    current_level.append(current_node.val)
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                levels.append(current_level)

            return levels
        
        return bfs_tree(root)
