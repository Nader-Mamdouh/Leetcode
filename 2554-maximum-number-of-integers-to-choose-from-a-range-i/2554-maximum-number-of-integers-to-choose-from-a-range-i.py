class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)  
        sm = 0
        count = 0
        for i in range(1, n + 1):
            if i not in banned:
                if sm + i > maxSum:
                    break
                sm += i
                count += 1
        return count
