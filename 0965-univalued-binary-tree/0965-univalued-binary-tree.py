# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        s=set()
        ans=[]
        def dfs(node):
            nonlocal ans
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        s=set(ans)
        if len(s)==1:
            return True
        else:
            return False    