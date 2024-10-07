class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx=max(nums)
        arr=[0]*(mx+1)
        for num in nums:
            arr[num]+=1
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]  
        mx2=max(arr)
        arr2=[0]*(mx2+1)
        for i in range(len(nums)):
            nm=nums[i]
            nm2=arr[nm]
            arr[nm]-=1
            arr2[nm2]=nums[i]
        return arr2[-1]    
