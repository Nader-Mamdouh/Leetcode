class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isgood(k):
            cnt=0
            for i in piles:
                cnt+=math.ceil(i/k)
            return cnt<=h    




        high=sum(piles)
        low=1
        while low<high:
            mid=(low+high)//2
            if isgood(mid):
                high=mid
            else:
                low=mid+1
        return high            