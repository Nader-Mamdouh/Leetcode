class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k<=numOnes:
            return k
        elif k<=(numOnes+numZeros):
            return numOnes
        else:
            x=(numOnes)
            count=numOnes+numZeros
            return x-(k-count)