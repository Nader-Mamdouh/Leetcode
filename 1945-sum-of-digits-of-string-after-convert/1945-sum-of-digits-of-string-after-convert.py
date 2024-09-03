class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss=""
        for char in s:
            ss+=str((ord(char) - ord('a')+1))
         
        for i in range(k):
            num=0
            for i in ss:
                num+=int(i)
            ss=str(num) 
        return num       



