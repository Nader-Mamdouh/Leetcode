class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        s=sorted(happiness,reverse=True)
        ans=0
        i=0
        while k:
            if (s[i]-i)<0:
                ans+=0
            else:
                ans+=s[i]-i
            k-=1
            i+=1

        return(ans)
        