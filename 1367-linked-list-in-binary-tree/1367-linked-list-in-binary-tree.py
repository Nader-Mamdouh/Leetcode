# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def dfs(node, head):
            if not head:  
                return True
            if not node: 
                return False
            if node.val != head.val:  
                return False
            
            return dfs(node.left, head.next) or dfs(node.right, head.next)
        
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
