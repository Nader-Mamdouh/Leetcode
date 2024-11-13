class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(1001)]
        size = [1 for i in range(1001)]
        n=len(isConnected)
        m=len(isConnected[0])
        ans=0
        def union(node1,node2):
            p1,p2 = find(node1),find(node2)

            if p1 == p2:
                return False

            if size[p1] > size[p2]:
                parents[p2] = p1
                size[p1] += size[p2]
            else:
                parents[p1] = p2
                size[p2] += size[p1]
                
            return True
        def find(node):
            if node == parents[node]:
                return node
            return find(parents[node])

        for i in range(n):
            for j in range(i+1,m):
                if isConnected[i][j] == 1:
                    union(i, j)
        return len(set(find(i) for i in range(n)))           