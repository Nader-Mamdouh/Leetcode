class Solution:
    def findComplement(self, num: int) -> int:
        binary_str = bin(num)[2:]
        s=""
        for i in binary_str:
            if i=='1':
                s+='0'
            else:
                s+='1'   
        number = int(s, 2)
        return number