class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        n = len(s)
        if n < 2:
            return s 
        longest_palindrome = ""
        for i in range(n):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i + 1)
            #print(odd_palindrome,even_palindrome,longest_palindrome)
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)

        return longest_palindrome
