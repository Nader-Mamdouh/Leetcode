class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bnr = bin(n)
        for i in range(1,len(bnr)):
            if bnr[i]==bnr[i-1]:
                return False
                
        return True        