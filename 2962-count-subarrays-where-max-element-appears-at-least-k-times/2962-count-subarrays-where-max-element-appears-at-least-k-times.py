class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxE = max(nums)
        
        n = len(nums)
        i = 0
        j = 0
        
        result = 0
        countMax = 0
        
        while j < n:
            if nums[j] == maxE:
                countMax += 1
            
            while countMax >= k:
                result += n - j
                
                if nums[i] == maxE:
                    countMax -= 1
                
                i += 1
            
            j += 1
        
        return result
        