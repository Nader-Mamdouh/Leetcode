class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        odd_count = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                k -= 1
                odd_count = 0
            while k == 0:
                if nums[l] % 2 == 1:
                    k += 1
                l += 1
                odd_count += 1
            count += odd_count
        return count      

