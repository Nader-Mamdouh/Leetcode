class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        ans=0
        if nums[0]==0 and n!=1:
            return False
        for i in range(n):
            further =i+nums[i]
            if further >=n or( nums[further]==0 and further!=n-1):
                further-=1
            if further==n-1:
                return True   
        return False         

