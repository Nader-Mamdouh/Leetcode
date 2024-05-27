class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            ans=0
            for j in range(len(nums)):  
                if i<=nums[j]:
                    ans+=1  
            if i==ans:
                return i 
        return -1                       
               
