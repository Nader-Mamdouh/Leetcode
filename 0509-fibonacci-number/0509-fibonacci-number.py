class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def fibb(x):
            if x in memo:
                return memo[x]
            elif x == 0:
                return 0
            elif x == 1:
                return 1
            else:
                memo[x] = fibb(x-1) + fibb(x-2)
                return memo[x]

        return fibb(n)
