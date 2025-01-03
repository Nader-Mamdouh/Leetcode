class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        prefix[0]=nums[0]
        suffix[n-1]=nums[-1]
        for i in range(1,n):
            prefix[i]+=nums[i]+prefix[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]=nums[i]+suffix[i+1]
        print(prefix)    
        print(suffix)
        for i in range(n-1):
            if prefix[i] >=suffix[i+1]:
                ans+=1
            
        return ans    