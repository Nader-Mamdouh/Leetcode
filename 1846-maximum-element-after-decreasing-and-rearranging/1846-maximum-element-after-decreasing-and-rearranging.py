class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        ans=0
        arr.sort()
        arr[0]=1
        for i in range(len(arr)):
            if arr[i]>arr[i-1]+1:
                arr[i]=arr[i-1]+1

        return max(arr)        