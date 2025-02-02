class Solution:
    def check(self, nums: List[int]) -> bool:
        arr=sorted(nums)
        n=len(nums)
        for i in range(n+1):
            if arr == nums[i::]:
                return True 
            else:
                x=nums[i]
                nums.append(x)
        return False