class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b1 = bin(x)[2:]
        b2 = bin(y)[2:]
        max_len = max(len(b1), len(b2))
        b1 = b1.zfill(max_len)
        b2 = b2.zfill(max_len)
        ans = 0
        for i in range(max_len):
            if b1[i] != b2[i]:
                ans += 1
                
        return ans
