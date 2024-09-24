class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        @cache
        def dp(index):
            if index>n:
                return float('inf')
            if index==n:
                return 0
            cs1=dp(index+1)+cost[index]
            cs2=dp(index+2)+cost[index] 
            return min(cs1,cs2)


        return min(dp(0),dp(1))               