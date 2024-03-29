

class Solution:
    def subarraysDivByK(self, nums, k):
        n = len(nums)
        remainder_count = {}
        count = 0
        cumulative_sum = 0

        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k

            if remainder == 0:
                count += 1

            if remainder in remainder_count:
                count += remainder_count[remainder]

            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count
