from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]*len(nums)
        i=len(nums)-1
        prev=0
        for n in reversed(nums):
            stack[i]=max(n,prev)
            prev=stack[i]
            i-=1
        print(stack)    
            
        ans=0
        l=0
        for r in range(len(nums)):
            while nums[l]>=stack[r]:
                l+=1
            ans=max(ans,r-l)
        return ans        
