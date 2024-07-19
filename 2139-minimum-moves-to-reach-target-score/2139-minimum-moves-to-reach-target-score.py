class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles==0:
            return target -1
        diff=target-1
        num=1
        x=target
        ans=0
        while maxDoubles and x>1:
            if x %2==0:
                x=x//2
                ans+=1
                maxDoubles-=1
            else:
                x-=1
                ans+=1  
        ans+=(x-1)          
        return ans        
                    