class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import defaultdict
        mdl=[]
        arr.sort()
        freq=defaultdict(int)
        ans=0
        n=len(arr)
        for i in arr:
            tmp=i%k
            mdl.append(tmp)
            freq[tmp]+=1
        for mod in range(k):
            if mod==0:
                if freq[mod]%2 !=0:
                    return False
            else:
                if freq[mod] != freq[k - mod]:
                    return False 
        return True                   

