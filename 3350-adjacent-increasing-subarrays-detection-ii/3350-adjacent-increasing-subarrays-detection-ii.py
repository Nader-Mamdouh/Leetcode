class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        mx=1
        pre_mx=0
        ans=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                mx+=1
            else:
                pre_mx=mx
                mx=1
            ans=max(ans,mx//2,min(mx,pre_mx))
        return ans  