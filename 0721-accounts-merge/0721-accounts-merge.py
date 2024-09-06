class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = [1] * 1001
        def union(u,v):
            rootX = find(u)
            rootY = find(v)
            if rootX != rootY:
                parent[rootY] = rootX
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])  
            return parent[u]
        dic = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(first_email, email)
                dic[email] = name
        components = defaultdict(list)
        for email in parent:
            root = find(email)
            components[root].append(email)        
        result = []
        for emails in components.values():
            result.append([dic[emails[0]]] + sorted(emails))
        
        return result