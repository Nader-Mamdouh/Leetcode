class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(candidates)
        def solve(i,cur):
            if i ==n:
                return
            if sum(cur)==target:
                res.append(cur[:])
                return
            elif sum(cur)>target: 
                return
            else:
                cur.append(candidates[i])         
                solve(i,cur)
                cur.pop() 
                solve(i+1,cur)    
        solve(0,[]) 
        return res      
