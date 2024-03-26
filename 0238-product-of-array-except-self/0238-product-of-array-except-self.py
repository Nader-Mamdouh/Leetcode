class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        suffix = []
        ans=[]
        for i in range(len(nums)):
            if i == 0:

                prefix.append(nums[i])
            else:
                prefix.append(nums[i] * prefix[i - 1])

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix.append(nums[i])
            else:
                suffix.append(nums[i] * suffix[-1])

        suffix=suffix[::-1]
        for i in range(len(nums)):
            if i==0:
                ans.append(suffix[i+1])
            elif i==len(nums)-1:
                ans.append(prefix[i-1])
            else:
                product=prefix[i-1]*suffix[i+1]
                ans.append(product)

        return(ans)

        