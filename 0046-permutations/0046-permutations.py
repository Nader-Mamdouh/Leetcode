class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cur=[]
        def solve():
            if len(cur)==len(nums):
                ans.append(cur[:])
                return 
            for i in nums:
                if i not in cur:
                    cur.append(i)     
                    solve()
                    cur.pop()
        solve()
        return ans            
    