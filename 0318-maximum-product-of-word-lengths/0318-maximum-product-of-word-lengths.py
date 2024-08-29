from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def get_bitmask(word: str) -> int:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            return bitmask
        
        n = len(words)
        bitmasks = [get_bitmask(word) for word in words]
        lengths = [len(word) for word in words]
        
        max_product = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0: 
                    max_product = max(max_product, lengths[i] * lengths[j])
        
        return max_product
