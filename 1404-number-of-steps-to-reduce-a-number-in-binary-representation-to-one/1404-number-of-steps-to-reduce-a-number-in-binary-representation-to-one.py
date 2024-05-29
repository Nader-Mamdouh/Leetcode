class Solution:
    def numSteps(self, s: str) -> int:
        s=s[::-1]
        num=0
        for i in range(len(s)):
            if s[i]=='1':
                num+=(2**i)
        #print(num)
        steps=0
        while num!=1:
            if num%2==0:
                num=num//2
            else:
                num+=1
            steps+=1 
        return steps                   
