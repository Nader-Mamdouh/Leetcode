class Solution:
    def maxScore(self, s: str) -> int:
        no1=s.count("1")
        mx=0
        left0=0
        right1=no1
        for i in range(len(s)-1):
            if s[i] =="0":
                left0+=1
            else:
                right1-=1
            mx=max(mx,left0+right1)
        return mx            