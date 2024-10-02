# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        arr=[]
        def dfs(node):
            if not node:
                return 
            arr.append(node.val)    
            dfs(node.left)
            dfs(node.right)    

        dfs(root)
        arr.sort()
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] :
                left = mid + 1
            else:
                right = mid

        return left+1
