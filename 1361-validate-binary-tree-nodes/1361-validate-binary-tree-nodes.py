class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        from collections import defaultdict,deque
        parent=defaultdict(list)
        child={}
        for node in range(n):
            left=leftChild[node]
            right=rightChild[node]
            if left !=-1:
                parent[node].append(left)
                if left not in child:
                    child[left]=node
                else:
                    return False
            if right !=-1:
                parent[node].append(right)
                if right not in child:
                    child[right]=node
                else:
                    return False   
        root=None
        for i in range(n):
            if i not in child:
                if not root:
                    root=i
                else:
                    return False
        if  root==None:
            return False
        visited=set()
        q=deque([root])
        while q:
            node=q.popleft()
            visited.add(node)
            for element in parent[node]:
                q.append(element)
        return len(visited)==n        

