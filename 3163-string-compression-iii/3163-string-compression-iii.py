from collections import defaultdict

class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        freq, n = 1, len(word)
        ch = word[0]
        for i in range(1, n):
            if word[i] == ch and freq < 9:
                freq += 1
            else:
                ans += str(freq) + ch
                ch = word[i]
                freq = 1
        ans += str(freq) + ch
        return ans