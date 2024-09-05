class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = [i for i in range(26)]
        size = [1 for i in range(26)]

        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return
            if size[par1] > size[par2]:
                parent[par2] = par1
                size[par1] += size[par2]
            else:
                parent[par1] = par2
                size[par2] += size[par1]

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])  
            return parent[node]

        for equation in equations:
            if '==' in equation:
                x, y = equation.split('==')
                union(ord(x) - 97, ord(y) - 97)
    
        for equation in equations:
            if '!=' in equation:
                x, y = equation.split('!=')
                if find(ord(x) - 97) == find(ord(y) - 97):  
                    return False
        
        return True        