class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
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
        return True if ans>=k else False                    