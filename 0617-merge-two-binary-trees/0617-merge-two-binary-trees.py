# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(r1,r2):
            if not r1 and not r2:
                return None
        
            if not r1:
                return r2
            if not r2:
                return r1
            if r1 and r2:
                r3=TreeNode(r1.val + r2.val)
                r3.left=solve(r1.left,r2.left)
                r3.right=solve(r1.right,r2.right)
            return r3    
                
        return solve(root1,root2)
            
