from typing import List, Dict, Tuple
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo: Dict[Tuple[int, int], int] = {}       
        def dfs(index: int, cur_amount: int) -> int:
            if cur_amount == amount:
                return 1
            if cur_amount > amount or index == len(coins):
                return 0
            if (index, cur_amount) in memo:
                return memo[(index, cur_amount)]
            include = dfs(index, cur_amount + coins[index])
            exclude = dfs(index + 1, cur_amount)
            memo[(index, cur_amount)] = include + exclude
            return memo[(index, cur_amount)]
        
        return dfs(0, 0)
