class Solution:
    def sortColors(self, array: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(array)
        for i in range(size):
            for j in range(size - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        