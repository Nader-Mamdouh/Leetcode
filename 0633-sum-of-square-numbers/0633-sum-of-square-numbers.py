from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(sqrt(c))
        
        while left <= right:
            total = left*left + right*right
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1
        
        return False
        