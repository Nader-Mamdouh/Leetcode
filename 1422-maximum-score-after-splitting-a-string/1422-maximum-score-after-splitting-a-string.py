class Solution:
    def maxScore(self, s: str) -> int:
        def solve(x):
            no1=0
            no0=0
            for i in range(x):
                if s[i]=='0':
                    no0+=1
            for i in range(x,len(s)):
                if s[i]=='1':
                    no1+=1   
            return no0+no1             
        n=len(s)
        mx=0
        for i in range(1,n):
            mx=max(mx,solve(i))
        return mx    
        