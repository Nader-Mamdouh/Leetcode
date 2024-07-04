class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        t=""
        for i in word1:
            s+=i
        for i in word2:
            t+=i  
        return s==t      
