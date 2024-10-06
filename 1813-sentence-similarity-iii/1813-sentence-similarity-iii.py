class Solution:
    def areSentencesSimilar(self,sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        i, j = 0, 0
        n1, n2 = len(words1), len(words2)
        while i < n1 and i < n2 and words1[i] == words2[i]:
            i += 1
        
        while j < n1 - i and j < n2 - i and words1[-j - 1] == words2[-j - 1]:
            j += 1
        return i + j >= min(n1, n2)
