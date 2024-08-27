class Solution:
    def count_ones(self,num: int) ->int:
        binary_rep = bin(num)
        count_ones = binary_rep.count('1')
        return count_ones
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            ans.append(self.count_ones(i))
        return ans    