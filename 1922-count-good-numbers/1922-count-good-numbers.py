class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod=10**9 + 7
        
        if n%2==0:
            return pow(4,(n//2),mod)*pow(5,(n//2),mod)%mod
        else:
            return pow(4,(n//2),mod)*pow(5,(n//2+1),mod)%mod

        