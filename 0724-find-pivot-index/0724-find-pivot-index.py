class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        running_sum = 0
        ans.append(0)
        
        for num in nums:
            running_sum += num
            ans.append(running_sum)
        
        left = 0
        right = len(ans) - 1 
        temp = 1

        while temp <= right:
            a = ans[temp] - ans[left]
            b = ans[right] - ans[temp - 1]  
            if a == b:
                return temp-1
            temp += 1

        return -1
