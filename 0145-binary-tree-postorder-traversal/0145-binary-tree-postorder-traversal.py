# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def solve(r):
            if r:
                
                solve(r.left)
                
                solve(r.right)
                ans.append(r.val)
        
        solve(root)
        return ans