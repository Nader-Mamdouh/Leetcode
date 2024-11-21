class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left=0
        n=len(nums)
        sm=0
        ans=float('inf')
        for right in range(n):
            sm+=nums[right]  
            while sm>=target:
                ans=min(ans,right-left+1)
                sm-=nums[left]
                left+=1 
                 
        return ans if ans != float('inf') else 0                