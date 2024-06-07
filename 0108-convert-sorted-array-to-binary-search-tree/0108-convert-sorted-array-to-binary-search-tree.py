# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        mid=len(nums)//2
        lefttree=self.sortedArrayToBST(nums[:mid])
        righttree=self.sortedArrayToBST(nums[mid+1:])
        return TreeNode(nums[mid],lefttree,righttree)    