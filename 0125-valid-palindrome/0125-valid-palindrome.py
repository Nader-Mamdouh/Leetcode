class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i.lower()>='a' and i.lower()<='z' or i=='0':
                t+=i.lower()  
        return (t==t[::-1])