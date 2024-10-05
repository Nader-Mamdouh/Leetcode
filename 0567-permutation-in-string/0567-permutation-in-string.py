class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from itertools import permutations
        n=len(s1)
        def get_permutations(input_str):
            perms = permutations(input_str)
            perm_list = [''.join(p) for p in perms]
            
            return perm_list
        pr=get_permutations(s1)
        for i in range(len(s2)-n+1):
            st=s2[i:i+n]
            if st in pr:
                return True
        return False        