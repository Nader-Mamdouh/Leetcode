class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = {0: 1} 
        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count
        