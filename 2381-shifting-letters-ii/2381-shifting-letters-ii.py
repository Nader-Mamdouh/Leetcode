class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        ranges = [0]*(n+1)
        for l,r,dirc in shifts:
            if dirc==1:
                ranges[l]+=1
                ranges[r+1]-=1
            elif dirc==0:
                ranges[l]-=1
                ranges[r+1]+=1
        for i in range (1,n+1):
            ranges[i]+=ranges[i-1]
        ans = ""
        for i in range(n):
            ans+=chr(((ord(s[i]) - ord('a') + ranges[i]) % 26) + ord('a'))
        return ans
        