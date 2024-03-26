class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ans = []
        running_sum = 0
        for num in nums:
            running_sum += num
            self.ans.append(running_sum)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.ans[right]
        else:
            return self.ans[right] - self.ans[left - 1]
