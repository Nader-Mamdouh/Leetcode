# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []
        bfs=[]
        q=deque([root])
        while q:
            level_size=len(q)
            level_sum=0
            for i in range(level_size):
                num=q.popleft()
                level_sum+=num.val
                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)  
            bfs.append(level_sum)          
        if len(bfs)>k:
            return max(bfs[k:])
        else:
            return -1        