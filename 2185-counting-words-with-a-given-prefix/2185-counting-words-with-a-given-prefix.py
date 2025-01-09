class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n=len(words)
        m=len(pref)
        ans=0
        for i in range(n):
            if pref == words[i][:m]:
                ans+=1
        return ans        