# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        node_count = 0
        
        def dfs(node):
            nonlocal node_count
            if not node:
                return
            node_count += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        return node_count
