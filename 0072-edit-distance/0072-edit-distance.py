from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @lru_cache(None)
        def dp(p1, p2):
            if p1 == n:  
                return m - p2
            if p2 == m: 
                return n - p1
            if word1[p1] == word2[p2]:
                return dp(p1 + 1, p2 + 1)

            insert_op = 1 + dp(p1, p2 + 1)     # Insert a character to match word2[p2]
            delete_op = 1 + dp(p1 + 1, p2)     # Delete a character from word1
            replace_op = 1 + dp(p1 + 1, p2 + 1)  # Replace word1[p1] with word2[p2]
            return min(insert_op, delete_op, replace_op)
        
        return dp(0, 0)
