class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        while n-1:
            v=""
            for i in range(len(s)):
                if s[i]=="1":
                    v+="0"
                else:
                    v+="1"
            vs=v[::-1]
            s=s+"1"+vs 
            #print(s)
            n-=1  
        return s[k-1]             