# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans=[-1,0]
        
        def solve(r,d):
            if d>self.ans[0] and r is not None:
                self.ans=[d,r.val]

            if r:
                
                solve(r.left,d+1)
                
                solve(r.right,d+1)
        
        solve(root,0)
        
        return self.ans[1]