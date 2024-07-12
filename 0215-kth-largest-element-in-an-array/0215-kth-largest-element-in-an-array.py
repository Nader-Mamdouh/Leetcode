import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-value for value in nums]
        heapq.heapify(max_heap)
        for i in range(len(nums)):
            max_value = -heapq.heappop(max_heap)
            if i==k-1:
                return max_value