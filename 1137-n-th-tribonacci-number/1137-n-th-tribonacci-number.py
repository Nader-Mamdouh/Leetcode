class Solution:
    def tribonacci(self, n: int) -> int:
        t0=0
        t1=1
        t2=1
        memo={0:1,1:1,2:1}
        
        def solve(x):
            
            if x==0:
                return t0
            if x==1 or x==2 :
                return t1
            if x in memo:
                return memo[x]  
            else:    
                memo[x]=solve(x-1)+solve(x-2)+solve(x-3)   
        return solve(n)    

