class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half: List[int], right_half: List[int]) -> List[int]:
            """Merge two sorted arrays into one sorted array."""
            result = []
            left_ptr, right_ptr = 0, 0
            
            while left_ptr < len(left_half) and right_ptr < len(right_half):
                if left_half[left_ptr] <= right_half[right_ptr]:
                    result.append(left_half[left_ptr])
                    left_ptr += 1
                else:
                    result.append(right_half[right_ptr])
                    right_ptr += 1
            
            # Append remaining elements
            result.extend(left_half[left_ptr:])
            result.extend(right_half[right_ptr:])
            
            return result

        def mergeSort(left: int, right: int, arr: List[int]) -> List[int]:
            """Merge sort implementation."""
            if left == right:
                return [arr[left]]  # Base case: single element
            
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            
            return merge(left_half, right_half)
        low=0
        high=len(nums)-1
        return mergeSort(low,high,nums)
