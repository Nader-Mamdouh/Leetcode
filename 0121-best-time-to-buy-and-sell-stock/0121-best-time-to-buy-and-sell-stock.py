class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=float('inf')
        mx=float('-inf')
        ans=0
        for i in range(len(prices)):
            mn=min(mn,prices[i])
            ans=max(ans,prices[i]-mn)
        return ans    
        