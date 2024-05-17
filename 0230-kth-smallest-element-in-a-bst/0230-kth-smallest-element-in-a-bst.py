# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def solve(r):
            if r==None:
                return
            
            solve(r.left)
            ans.append(r.val)
            solve(r.right)
         
        solve(root) 
        
        return ans[k-1]  