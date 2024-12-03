class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        j=0
        for i in spaces:
            if j!=0:
                i+=j
            s=s[:i]+" "+s[i:]
            j+=1
            
        return s   