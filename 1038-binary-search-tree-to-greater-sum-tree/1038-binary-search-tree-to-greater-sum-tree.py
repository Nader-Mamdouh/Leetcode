# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        summ = 0

        def dfs(node):
            nonlocal summ
            if not node:
                return
            dfs(node.right)
            summ += node.val
            node.val = summ
            dfs(node.left)

        dfs(root)
        return root 
            