from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = nums1[:m]
        left = 0
        right = 0
        ans = []
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                ans.append(nums1[left])
                left += 1
            else:
                ans.append(nums2[right])
                right += 1

        if left < m:
            ans.extend(nums1[left:])
        if right < n:
            ans.extend(nums2[right:])

       
        nums1[:] = ans  
