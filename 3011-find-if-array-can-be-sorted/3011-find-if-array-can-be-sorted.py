class Solution:
    def haveSameSetBits(self, a: int, b: int) -> bool:
        return bin(a).count('1') == bin(b).count('1') 
        
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums) 
        for _ in range(n):
            for i in range(n- 1):
                if self.haveSameSetBits(nums[i], nums[i + 1]) and nums[i + 1] < nums[i]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        return nums == sorted(nums)
