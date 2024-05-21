from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            new_subsets = [curr + [num] for curr in ans]
            ans.extend(new_subsets)
        return ans
