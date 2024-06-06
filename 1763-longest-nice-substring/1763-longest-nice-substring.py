class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        s_st = set(s)
        
        for i, c in enumerate(s):
            if c.lower() not in s_st or c.upper() not in s_st:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        
        return s
