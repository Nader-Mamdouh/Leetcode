class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=0
        for i in range(len(nums)):
            leftsum=sum(nums[:i+1])
            rightsum=sum(nums[i:])
            if leftsum==rightsum:
                return i
        return -1        