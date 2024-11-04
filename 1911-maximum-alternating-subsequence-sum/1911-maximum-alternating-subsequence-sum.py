class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sumeven=0
        sumodd=0
        for i in range(len(nums)-1,-1,-1):
            tmpeven=max(sumodd+nums[i],sumeven)
            tmpodd=max(sumeven-nums[i],sumodd)
            sumeven=tmpeven
            sumodd=tmpodd
        return sumeven    