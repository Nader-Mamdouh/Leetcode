class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        right=len(nums)-1
        while low<=right:
            mid=(low+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                right=mid-1
        return low     