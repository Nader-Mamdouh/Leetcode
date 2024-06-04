class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        
        for char in s:
            dic[char] += 1
        
        ans = 0
        has_odd = False
        
        for value in dic.values():
            if value % 2 == 0:
                ans += value
            else:
                ans += value - 1
                has_odd = True
        
        if has_odd:
            ans += 1
        
        return ans
