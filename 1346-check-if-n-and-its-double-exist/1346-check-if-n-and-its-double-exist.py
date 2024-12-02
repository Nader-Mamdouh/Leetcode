class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if i*2 in arr and i !=0:
                return True
        return False        