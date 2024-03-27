class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        max_length = 0
        current = 1
        left = 0
        n=len(word)
        while left < n:
            right = left + 1
            while right < len(word) and word[right] >= word[right-1]:
                current += 1
                right += 1
            if len(set(word[left:right])) == 5:
                max_length = max(max_length, current)
            current = 1
            left = right
        return max_length