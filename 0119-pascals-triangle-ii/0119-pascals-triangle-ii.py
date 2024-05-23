from math import factorial
from typing import List

class Solution:
    def getRow(self, n: int) -> List[int]:
        def binomial_coefficient(n: int, k: int) -> int:
            return factorial(n) // (factorial(k) * factorial(n - k))
        
        return [binomial_coefficient(n, i) for i in range(n + 1)]


