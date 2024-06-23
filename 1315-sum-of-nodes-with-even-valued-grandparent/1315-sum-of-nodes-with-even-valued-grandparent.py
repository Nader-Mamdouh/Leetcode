# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        summ2=0  
        k=0 
        def dfs(node,parent,grand):
            if node==None:
                return 0
            summ = 0
            if grand and grand.val % 2 == 0:
                summ += node.val
            summ += dfs(node.left, node, parent)
            summ += dfs(node.right, node, parent)
            return summ    


        return dfs(root,None,None)       
