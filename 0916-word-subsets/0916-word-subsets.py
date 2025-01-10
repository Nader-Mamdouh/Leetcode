from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                required[char] = max(required[char], count)
        
        ans = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= required[char] for char in required):
                ans.append(word)
        
        return ans
