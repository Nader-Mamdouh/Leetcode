class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def generateMid(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            return TreeNode(nums[mid], generateMid(nums[:mid]), generateMid(nums[mid+1:]))       
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)     
        arr = inorder(root)
        return generateMid(arr)
