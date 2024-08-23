class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        n = len(nums)
        length = [1] * n
        count = [1] * n
        max_length = 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] <= length[j]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[i] == length[j] + 1:
                        count[i] += count[j]
            
            max_length = max(max_length, length[i])
        
        result = 0
        for i in range(n):
            if length[i] == max_length:
                result += count[i]
        
        return result