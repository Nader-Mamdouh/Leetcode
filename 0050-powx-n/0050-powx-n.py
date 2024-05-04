class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            return self.pow_helper(x, n)
    
    def pow_helper(self, x: float, n: int) -> float:
        if n == 1:
            return x
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
