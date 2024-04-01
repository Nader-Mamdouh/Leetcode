class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        s = s.rstrip()

        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                ans += 1
            else:
                break

        return(ans)
        