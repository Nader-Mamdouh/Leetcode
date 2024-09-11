# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import defaultdict
        if not k :
            return [target.val]
        graph = defaultdict(list)
        queue= deque([root])   
        while queue:
            node=queue.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node) 
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right) 
        res=[]
        vis=set([target]) 
        q=deque([(target,0)])  
        while q:
            node,dis=q.popleft()
            if dis==k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in vis:
                        vis.add(edge)
                        q.append((edge,dis+1))
        return res                                 

         
                   