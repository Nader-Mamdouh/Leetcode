class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        if len(s)==k:
            return True
        ct =Counter(s)
        ans=0
        for ch,fr in ct.items():
            if fr %2 ==1:
                ans+=1
        if ans>k:
            return False
        return True
