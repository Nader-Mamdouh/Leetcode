class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import defaultdict
        count=defaultdict(int)
        for i in arr1:
            count[i]+=1
        result=[]
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]
        for num in sorted(count):
            result.extend([num] * count[num])   

        return result            