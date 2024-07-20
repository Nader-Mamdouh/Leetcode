# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        ans=0
        def solve (node,steps):
            nonlocal ans
            if node==None:
                ans=max(ans,steps)
                return 
            solve(node.left,steps+1)   
            solve(node.right,steps+1)
        solve(root,0)
        return ans        