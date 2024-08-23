from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(x + y) - int(y + x)
        
        nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)
        largest_num = "".join(nums)
        return "0" if largest_num[0] == "0" else largest_num
