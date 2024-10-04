from typing import List
from collections import defaultdict

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        
        # If the total sum is divisible by p, no subarray needs to be removed
        if remainder == 0:
            return 0
        
        # Dictionary to store the most recent index of a given prefix sum modulo p
        prefix_map = {0: -1}  # Prefix sum modulo p that makes it divisible
        prefix_sum = 0
        min_length = len(nums)  # Start with max length
        
        for i, num in enumerate(nums):
            # Update the prefix sum
            prefix_sum = (prefix_sum + num) % p
            
            # Find what prefix sum we need to remove (prefix_sum - remainder) % p
            target = (prefix_sum - remainder) % p
            
            # Check if we've seen this prefix sum remainder before
            if target in prefix_map:
                # Calculate the subarray length to be removed
                min_length = min(min_length, i - prefix_map[target])
            prefix_map[prefix_sum] = i
        return min_length if min_length < len(nums) else -1
