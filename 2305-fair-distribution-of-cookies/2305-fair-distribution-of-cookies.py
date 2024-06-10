class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        fairness = float('inf')
        def backtrack(cookie, children):
            # base
            nonlocal fairness
            if cookie == len(cookies):
                fairness = min(fairness, max(children))
                return
                #pass
            for i in range(k):
                children[i] += cookies[cookie]
                if max(children) < fairness:
                    backtrack(cookie + 1, children)
                children[i] -= cookies[cookie]
        backtrack(0, [0] * k)
        return fairness