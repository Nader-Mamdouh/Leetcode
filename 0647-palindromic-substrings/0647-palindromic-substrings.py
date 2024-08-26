class Solution:
    def ispal(self,s2:str)->bool:
        return s2==s2[::-1]
    def countSubstrings(self, s: str) -> int:
        substrings = []
        n = len(s)
        ans=0
        for i in range(n):
            for j in range(i + 1, n + 1):
                substrings.append(s[i:j])
        for sub in substrings:
            if self.ispal(sub):
                ans+=1
        return ans        
