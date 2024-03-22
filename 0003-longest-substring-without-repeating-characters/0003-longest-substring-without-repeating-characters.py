from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = 0
        max_length = 0
        dic = defaultdict(int)
        
        for right in range(n):
            dic[s[right]] += 1
            
            while dic[s[right]] > 1:
                dic[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
