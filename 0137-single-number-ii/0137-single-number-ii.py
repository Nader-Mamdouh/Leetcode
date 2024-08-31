class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        y = 0
        for num in nums:
            x ^= (num & ~y)
            y ^= (num & ~x)
        return x